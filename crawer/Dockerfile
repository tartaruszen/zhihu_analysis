FROM ubuntu-upstart

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "craw_worker.py"]
