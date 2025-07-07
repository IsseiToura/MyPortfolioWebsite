from langgraph.graph import END, START, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from .tools import tools
from .model import gpt_model
from .rag import rag_retrieve

# === prompt template ===
template = """
You are Issei's best friend and a good assistant named Nisei who answers questions using the provided document snippets and tools.
Use the document snippets to answer the question, or use the "search" tool if necessary.
Please answer as Nisei, not Issei.

Document snippets: {document_snippet}

Question: {question}

Answer:

"""

def preprocess_message(question: str):
    document_snippet = rag_retrieve(question)
    content = template.format(document_snippet=document_snippet, question=question)
    print(f"preprocess_message content: {content}")
    return [HumanMessage(content=content)]

def call_model(state: MessagesState):
    messages = state['messages']
    print(f"call model messages: {messages}")
    response = gpt_model.bind_tools(tools).invoke(messages)
    print(f"call model response: {response}")
    return {"messages": [response]}

def should_continue(state: MessagesState):
    messages = state['messages']
    last_message = messages[-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    if hasattr(last_message, 'content') and "search" in last_message.content:
        return "tools"
    return END

# === build workflow ===
workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", ToolNode(tools))
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
)
workflow.add_edge("tools", 'agent')
checkpointer = MemorySaver()
app_flow = workflow.compile(checkpointer=checkpointer)
