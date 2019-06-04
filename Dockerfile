FROM ubuntu:18.04
COPY app/*  ./app/
RUN apt-get update && apt-get install -y python python-pip wget && pip install Flask
CMD python /app/webs.py
