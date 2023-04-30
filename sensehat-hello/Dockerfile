# https://docs.balena.io/reference/base-images/base-images/
FROM balenalib/raspberrypi3-alpine-python:run

RUN install_packages sense-hat

WORKDIR /app

COPY hello.py hello.py

CMD [ "python", "hello.py" ]