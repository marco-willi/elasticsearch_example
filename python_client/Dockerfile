FROM python:3

WORKDIR /usr/src/app

RUN pip install elasticsearch

COPY process.py ./

CMD ["python", "./process.py"]