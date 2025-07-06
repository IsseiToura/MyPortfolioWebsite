from .document_loader import db
from .model import gpt_embeddings

def rag_retrieve(question: str):
    """
    Retrieve relevant document chunks based on the question.
    
    Args:
        question (str): The user's question
        
    Returns:
        str: Concatenated relevant document content
    """
    question_embedding = gpt_embeddings.embed_query(question)
    
    # Retrieve top 3 most similar document chunks
    docs = db.similarity_search_by_vector(question_embedding, k=3)
    
    # Combine the content of retrieved documents
    if docs:
        combined_content = "\n\n".join([doc.page_content for doc in docs])
        return combined_content
    else:
        return "No related information found."
