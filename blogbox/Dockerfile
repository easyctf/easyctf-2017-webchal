FROM python:3-onbuild
MAINTAINER Jacob Magnuson <me@jacobmagnuson.com>

RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app/

ENTRYPOINT ["python"]
CMD ["app.py"]
