FROM ubuntu:18.04
COPY * /app
RUN python /app/webs.py
