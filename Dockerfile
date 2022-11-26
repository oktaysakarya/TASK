FROM python:latest as builder

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

COPY  ./IHA /app

WORKDIR /app

RUN pip3 install --upgrade pip

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./komutlar.sh /

ENTRYPOINT [ "sh", "/komutlar.sh" ]
