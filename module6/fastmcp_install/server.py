#python -m pip install fastmcp
from fastmcp import FastMCP

mcp = FastMCP("AnswerServer")

@mcp.tool
def explain() -> str:
    return "This server understands 42"