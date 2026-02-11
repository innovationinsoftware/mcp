from fastmcp import FastMCP

mcp = FastMCP("Hello World")

# define the tool
@mcp.tool()
def hello_world(name: str) -> str:
    return f"Hello World. This is {name} 👋"

# entry point - not needed but suggested
if __name__ == '__main__':
    mcp.run(transport = 'stdio')