# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /usr/src/reapr-web
COPY requirements.txt . 
RUN apt update
RUN apt-get install -y unixodbc-dev
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
