import os
from signalbot import SignalBot, Command, Context
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
)


def ask_chatGPT(message: str):
    response = client.responses.create(
        model="gpt-4o",
        #instructions="Gerda Blau ist vor kurzem gestorben. Du wirst von Angehörigen angeschrieben. Hilf Ihnen dabei ein paar Bilder oder einen kleinen Text zu Gerda zu schreiben.",
        instructions="Erzähle interessante Dinge, damit die Leute beschäftigt werden",
        input=message
    )
    return(response)

class PingCommand(Command):
    async def handle(self, c: Context):
       answer = ask_chatGPT(c.message.text)
       print(answer.output_text)
       await c.send(answer.output_text)



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