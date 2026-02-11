from fastmcp import FastMCP

mcp = FastMCP("HelloServer")

@mcp.tool
def hello() -> str:
    return "Hello, World!"

if __name__ == "__main__":
    # HTTP server
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )
