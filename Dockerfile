# Dockerfile para la practica 1 de TCVD

FROM python:3.8-slim-buster
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install requests
COPY . .
# CMD [ "python3", "generate.py"]
ENTRYPOINT ["python3"]