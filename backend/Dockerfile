FROM python:latest
RUN apt-get update -q
RUN pip install flask
WORKDIR /usr/src/app/
COPY . ./
CMD [ "python", "./main.py"]