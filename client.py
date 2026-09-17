import mcp.types as types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uv",
    args=["run", "server.py"],
)


async def message_handler(message):
    if isinstance(message, Exception):
        print(f"Error: {message}")
        return

    if not hasattr(message, "root"):
        return

    match message.root:
        case types.LoggingMessageNotification(params=params):
            print(params.data)
        case types.ProgressNotification(params=params):
            if params.total is not None:
                percentage = (params.progress / params.total) * 100
                print(f"Progress: {params.progress}/{params.total} ({percentage:.1f}%)")
            else:
                print(f"Progress: {params.progress}")
        case _:
            pass


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, message_handler=message_handler) as session:
            await session.initialize()
            result = await session.call_tool(name="add", arguments={"a": 1, "b": 3})
            print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
