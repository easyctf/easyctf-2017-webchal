FROM python:2-onbuild
MAINTAINER Michael Zhang <me@michaelz.xyz>

RUN pip install flask pillow
COPY . /app
WORKDIR /app/

ENTRYPOINT ["python"]
CMD ["app.py"]
