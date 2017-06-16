FROM python:2.7.12

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "text_web.py"]
CMD ["python", "text_worker.py"]
