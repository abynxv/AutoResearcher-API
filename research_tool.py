from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 5) -> str:
    """
    Searches the web using DuckDuckGo and returns a formatted string of the results.
    """
    print(f"  [Tool Executing] -> searching web for: '{query}'")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            
        if not results:
            return "No results found."
            
        formatted_results = []
        for idx, result in enumerate(results):
            title = result.get('title', 'No Title')
            href = result.get('href', 'No URL')
            body = result.get('body', 'No snippet')
            
            formatted_results.append(
                f"Result {idx+1}:\n"
                f"Title: {title}\n"
                f"URL: {href}\n"
                f"Snippet: {body}\n"
                f"{'-'*20}"
            )
            
        return "\n".join(formatted_results)
    
    except Exception as e:
        return f"Error executing web search: {e}"

# Tool schema for the LLM
search_tool_schema = {
    "type": "function",
    "function": {
        "name": "search_web",
        "description": "Searches the internet for up-to-date information on a given topic. Returns snippets from top web pages.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to look up on the internet.",
                }
            },
            "required": ["query"],
        },
    }
}
