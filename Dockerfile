FROM python:3.8-slim-buster

RUN mkdir /flask-project-docker

COPY requirements.txt /flask-project-docker/requirements.txt
COPY flask-proj.py /flask-project-docker/flask-proj.py

RUN pip3 install -r /flask-project-docker/requirements.txt

EXPOSE 5000

CMD [ "python3", "/flask-project-docker/flask-proj.py"]
