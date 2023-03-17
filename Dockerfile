FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /home/app
COPY requirements.txt /home/app/
RUN pip install -r requirements.txt
COPY . /home/app/
