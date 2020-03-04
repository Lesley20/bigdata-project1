FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install sodapy

RUN pip freeze > requirements.txt