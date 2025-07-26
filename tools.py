import os
import datetime
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()  # Load from .env

# Read API key from environment
tavily_api_key = os.getenv("TAVILY_API_KEY")

# ✅ Pass the key explicitly
search_tool = TavilySearchResults(tavily_api_key=tavily_api_key)

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Returns the current system time in the specified format."""
    now = datetime.datetime.now()
    return now.strftime(format)

tools = [search_tool, get_system_time]
