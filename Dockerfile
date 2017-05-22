FROM python:3.6.1

COPY . .

RUN pip install nltk
