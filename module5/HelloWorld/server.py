from fastmcp import FastMCP

mcp = FastMCP("HelloWorldServer")

@mcp.resource("hello://world")
def hello_world():
    return "Hello, world!"

if __name__ == "__main__":
    mcp.run()