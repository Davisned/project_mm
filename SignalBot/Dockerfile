FROM python:3.11-slim

ENV PHONE_NUMBER2="+49123456789"

ENV API_KEY="asdfasdfasdfasdf"

ENV PORT_OF_SIGNAL_REST_CLI_SERVER="192.168.137.1:9922"

COPY SignalOpenAI.py ./

COPY .env ./

RUN pip install openai

RUN pip install dotenv

RUN pip install signalbot

CMD ["python3", "SignalOpenAI.py"]