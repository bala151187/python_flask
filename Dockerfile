FROM ubuntu:18.04
COPY requirements.txt *.py  /app
RUN python /app/webs.py
