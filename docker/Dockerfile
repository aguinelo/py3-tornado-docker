FROM python:3.6
LABEL maintainer="aguinelo@dreibox.com"

EXPOSE 8001

RUN mkdir -p /app
WORKDIR /app

ADD src /app/
RUN pip install -r requirements.txt

CMD python main.py