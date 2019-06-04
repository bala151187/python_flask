FROM ubuntu:18.04
ADD requirements.txt webs.py  /app
RUN python /app/webs.py
