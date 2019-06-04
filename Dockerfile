FROM ubuntu:18.04
ADD requirements.txt *.py  /app
RUN python /app/webs.py
