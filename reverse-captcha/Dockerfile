FROM ubuntu:12.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python python-pip python-virtualenv gunicorn
RUN apt-get install -y libjpeg-dev libpng-dev zlib1g-dev python-dev

RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
RUN pip install -r /deploy/app/requirements.txt
WORKDIR /deploy/app

EXPOSE 80
CMD ["/usr/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "app:app"]