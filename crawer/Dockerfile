FROM python:2.7.13

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "craw_worker.py"]
