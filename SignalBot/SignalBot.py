import os
from signalbot import SignalBot, Command, Context


class PingCommand(Command):
    async def handle(self, c: Context):
        print("Nachricht da")
#        if c.message.text == "Ping":
#            await c.send("Pong")


if __name__ == "__main__":
    bot = SignalBot({
        "signal_service": '127.0.0.1:8080',
        "phone_number": ""
    })
    bot.register(PingCommand()) # all contacts and groups
    bot.start()