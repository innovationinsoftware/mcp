from fastmcp import FastMCP

mcp = FastMCP("math-tools")

@mcp.tool("factorial")
def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    if not isinstance(n, int):
        raise TypeError("factorial() expects an int")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool("cubed")
def cubed(x):
    """Return x^3."""
    return x ** 3

if __name__ == "__main__":
    mcp.run()