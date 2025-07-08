from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_web_tool(query: str) -> str:
    """
    Searches the web and returns results.
    """
    try:
        search_tool = DuckDuckGoSearchResults(num_results=10, verbose=False)
        result = search_tool.run(query)
        # Ensure the result is a string for CrewAI compatibility
        return str(result)
    except Exception as e:
        # Return a clear error message for debugging and CrewAI logs
        return f"Search failed: {e}"
