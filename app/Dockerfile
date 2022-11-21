FROM python:3.8
ENV PYTHONBURRERED=1
WORKDIR /django
RUN apt-get update && apt-get -y install mdbtools
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
