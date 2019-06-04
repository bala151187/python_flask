FROM ubuntu:18.04
COPY app/*  ./app/
RUN python /app/webs.py
