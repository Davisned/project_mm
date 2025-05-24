import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

agent = Agent(name="Assistant", instructions="Your are a helpful assistant")
    
class PingCommand(Command):
    async def handle(self, c: Context):
       answer = await Runner.run(agent,c.message.text)
       await c.send(answer.final_output)

def start_signal_bot():
    bot = SignalBot(config={
        "signal_service": os.getenv("PORT_OF_SIGNAL_REST_CLI_SERVER"),
        "phone_number": os.getenv("PHONE_NUMBER2")
    })
    print(bot.config)
    bot.register(PingCommand()) # all contacts and groups
    bot.start()

if __name__ == "__main__":
    start_signal_bot()