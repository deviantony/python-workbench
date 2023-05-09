# https://docs.balena.io/reference/base-images/base-images/
FROM balenalib/raspberrypi3-debian-python:build

RUN install_packages sense-hat python3-dev

WORKDIR /src/
RUN git clone --depth 1 -b V7.2.1 https://github.com/RPi-Distro/RTIMULib/
WORKDIR /src/RTIMULib/Linux/python/
RUN python setup.py build
RUN python setup.py install

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY sensehat.py ./

CMD [ "python", "sensehat.py" ]