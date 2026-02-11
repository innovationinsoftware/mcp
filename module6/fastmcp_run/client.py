from fastmcp import Client
import asyncio

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool("hello", {})
        print(result.content[0].text)

asyncio.run(main())