FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY ./src /code
COPY requirements.txt  /code/
RUN pip install -r requirements.txt


CMD python3 manage.py runserver 0.0.0.0:$PORT
