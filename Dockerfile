FROM ubuntu:18.04
COPY * /app
ADD webs.py /app
RUN python /app/webs.py
