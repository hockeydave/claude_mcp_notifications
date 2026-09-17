import asyncio
import logging

from mcp.server.mcpserver import MCPServer, Context

logger = logging.getLogger("Demo Server")

mcp = MCPServer("Demo Server")


@mcp.tool()
async def add(a: int, b: int, ctx: Context) -> int:
    logger.info("Preparing to add...")
    await ctx.report_progress(20, 100)
    await asyncio.sleep(2)
    logger.info("OK, adding...")
    await ctx.report_progress(80, 100)
    return a + b


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    mcp.run()
