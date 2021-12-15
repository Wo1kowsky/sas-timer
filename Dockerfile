FROM python:3.9.6-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat

RUN pip install --upgrade pip
COPY . .
RUN rm -rf ./venv
RUN pip install -r requirements.txt
EXPOSE 8000
# CMD ["gunicorn", "app:app.server", "-b", "0.0.0.0:8000"]
