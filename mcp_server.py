from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Utility MCP Server")


# -----------------------------
# Calculator Tool
# -----------------------------
@mcp.tool()
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    Example: 25 * 10
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"

    except Exception:
        return "Invalid mathematical expression."


# -----------------------------
# Text Analyzer Tool
# -----------------------------
@mcp.tool()
def text_analyzer(text: str) -> str:
    """
    Analyze text and return basic statistics.
    """

    characters = len(text)
    words = len(text.split())
    sentences = len([
        sentence for sentence in text.split(".")
        if sentence.strip()
    ])

    return (
        f"Characters: {characters}\n"
        f"Words: {words}\n"
        f"Sentences: {sentences}"
    )


# -----------------------------
# File Reader Tool
# -----------------------------
@mcp.tool()
def read_file(file_path: str) -> str:
    """
    Read the contents of a text file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except Exception as e:
        return f"Error reading file: {str(e)}"


# -----------------------------
# Run MCP Server
# -----------------------------
if __name__ == "__main__":
    mcp.run()