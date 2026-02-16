from fastmcp import FastMCP

mcp = FastMCP("Summation Server")

@mcp.tool
def summation(n: int) -> int:
    """
    Return the summation 1 + 2 + ... + n.

    Inputs:
      n (int): must be >= 0

    Output:
      int: sum from 1 to n
    """
    if n < 0:
        raise ValueError("n must be >= 0")

    # Uses the closed-form formula: n(n+1)/2
    return n * (n + 1) // 2

if __name__ == "__main__":
    mcp.run()