from mcp.server.mcpserver import MCPServer, Context
import asyncio
mcp = MCPServer(name="Demo Server")
@mcp.tool()
async def add(a: int, b: int, ctx: Context) -> int:
    await ctx.info("Preparing to add...")
    await ctx.report_progress(20, 100)
    await asyncio.sleep(2)
    await ctx.info("OK, adding...")
    await ctx.report_progress(80, 100)
    return a + b
