import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a nice guy",
    input="Hello tell me something sad."
)

print(response.output_text)