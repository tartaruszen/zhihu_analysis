FROM ubuntu-upstart

RUN apt-get update
RUN apt-get install -y --force-yes python python-dev python-setuptools software-properties-common gcc python-pip
RUN apt-get clean all

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "text_web.py"]
CMD ["python", "text_worker.py"]
