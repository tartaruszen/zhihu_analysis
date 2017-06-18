FROM python:2.7.12

ADD . /library
WORKDIR /library
RUN pip install -r requirements.txt
WORKDIR /code
