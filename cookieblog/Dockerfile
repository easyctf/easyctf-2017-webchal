FROM tutum/lamp:latest
EXPOSE 80
RUN a2enmod rewrite
RUN rm -rf /app/*
COPY . /app/
CMD '/run.sh'