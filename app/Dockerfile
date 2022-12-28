FROM python:3.8
ENV PYTHONBURRERED=1
WORKDIR /django
RUN apt-get update && apt-get -y install mdbtools
COPY requirements.txt requirements.txt
RUN pip uninstall PyYAML
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
