import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv

class PingCommand(Command):
    async def handle(self, c: Context):
        #if c.message.text == "Ping":
       await c.send("Pong")


if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("PHONE_NUMBER2"))
    bot = SignalBot(config={
        "signal_service": '192.168.137.1:9922',
        "phone_number": os.getenv("PHONE_NUMBER2")
    })
    print(bot.config)
    bot.register(PingCommand()) # all contacts and groups
    bot.start()
    print(os.getenv("PHONE_NUMBER"))