import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp.server import MCPServerSse

load_dotenv()


mcp_server = MCPServerSse(
    params={
        "url": str(os.getenv("SIGNALBOT_MCP_URL", "http://localhost:8000/mcp")),
    },
    cache_tools_list=True,
    name="Project MM MCP Server",
)

agent = Agent(name="Assistant", instructions="Your are a helpful assistant", mcp_servers=[mcp_server])


class PingCommand(Command):
    async def handle(self, c: Context):
        async with mcp_server:
            # tools = await mcp_server.list_tools()
            # tool_txt = "Available tools from MCP server:"
            # for tool in tools:
            #     tool_txt += f"\n- {tool.name} ({tool.description})"
            answer = await Runner.run(agent, c.message.text)
            await c.send(answer.final_output)  # f"""{tool_txt}\n\n{answer.final_output}""")


def start_signal_bot():
    bot = SignalBot(
        config={
            "signal_service": os.getenv("SIGNAL_CLI_REST_API_URL"),
            "phone_number": os.getenv("SIGNALBOT_PHONE_NUMBER"),
        }
    )
    print(bot.config)
    bot.register(PingCommand())  # all contacts and groups
    bot.start()


if __name__ == "__main__":
    print("Starting Signal Bot...")
    start_signal_bot()
