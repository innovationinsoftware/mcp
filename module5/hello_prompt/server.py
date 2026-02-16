from fastmcp import FastMCP

mcp = FastMCP("HelloPromptServer")

@mcp.prompt("hello_prompt")
def hello_prompt():
    return {
        "description": "A simple hello world prompt",
        "messages": [
            {
                "role": "user",
                "content": "Say hello to the user in one friendly sentence."
            }
        ]
    }

if __name__ == "__main__":
    mcp.run() # per client
