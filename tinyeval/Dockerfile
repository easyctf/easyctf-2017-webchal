FROM tutum/lamp:latest
EXPOSE 80
RUN sed -i 's/AllowOverride FileInfo/AllowOverride All/' /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod rewrite
RUN rm -rf /app/*
COPY . /app/
RUN printf "<Files ~ \"^flag(.+)$\">\nOrder allow,deny\nDeny from all\n</Files>" > .htaccess
CMD '/run.sh'