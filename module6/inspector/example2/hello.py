from fastmcp import FastMCP

mcp = FastMCP("Hello World 2")

# define the tool
@mcp.tool
def hello_world(name: str) -> str:
    return f"Hello World. This is {name} 👋"

@mcp.tool
def hello_chicago() -> str:
    return f"Hello from the Windy City"


@mcp.resource("data://hometown")
def hometown() -> str:
    return "Neptune, NJ"

# entry point - not needed but suggested
if __name__ == '__main__':
    mcp.run(transport = 'stdio')