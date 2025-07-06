from flask import request, jsonify, g
from .workflow import app_flow, preprocess_message
from flask import Blueprint

issei_gpt_bp = Blueprint('issei_gpt', __name__, url_prefix='/api/issei_gpt')


@issei_gpt_bp.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]
    inputs = preprocess_message(question)
    thread = {"configurable": {"thread_id": "42"}}
    for event in app_flow.stream({"messages": inputs}, thread, stream_mode="values"):
        response = event["messages"][-1].content
    search_results = getattr(g, "search_results", [])
    links = "\n".join(search_results) if search_results else "No related links found"
    print(f"response: {response}")
    return jsonify({"answer": response, "links": links})
