from langchain_core.tools import tool
from flask import g
from serpapi import GoogleSearch
import config

@tool
def search(query: str):
    """Use SerpAPI to perform web search."""
    params = {
        "q": query,  # search query
        "hl": "en",  # language setting (English)
        "gl": "us",  # region setting (United States)
        "api_key": config.SERP_API_KEY  # SerpAPI API key
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    results_list = result.get("organic_results", [])
    search_results = [
        f"{res['title']}: {res['snippet']} - {res['link']}" for res in results_list[:3]
    ]
    g.search_results = search_results if search_results else ["No search results found."]
    print(f"search results: {g.search_results}")
    return g.search_results

tools = [search]
