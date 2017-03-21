FROM python:3-onbuild
MAINTAINER Michael Zhang <me@michaelz.xyz>

RUN pip install flask pymysql
COPY . /app
WORKDIR /app/

ENTRYPOINT ["python"]
CMD ["app.py"]
