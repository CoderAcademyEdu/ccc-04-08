FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3.8 -y

WORKDIR /code

COPY src .

RUN apt-get install python3-pip -y

RUN pip3 install -r requirements.txt

ENV FLASK_APP=main:create_app

CMD [ "flask", "run", "-h", "0.0.0.0" ]