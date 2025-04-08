import httpx
from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup

mcp = FastMCP(
    'Your MCP Tools',
    dependencies=['beautifulsoup4'],
)

@mcp.tool(
    name='extract-web-page-content',
    description='Extracts the content of a web page using BeautifulSoup.'
)
def extract_web_page_content(url: str) -> str | None:
    """
    Extracts the content of a web page using BeautifulSoup.
    """

    try:
        response = httpx.get(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            },
            timeout=10.0,  # Set a timeout for the request
            follow_redirects=True
        )
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text().replace('\n', ' ').replace('\r', ' ').strip()  # Return the text content of the page
    except Exception as e:
        return f"Error fetching page: {e}"  # Return the error message
    

if __name__ == "__main__":
   mcp.run(transport='stdio')