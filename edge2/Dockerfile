FROM tutum/lamp:latest
RUN apt-get update && apt-get install -y git
EXPOSE 80
RUN sed -i 's/AllowOverride FileInfo/AllowOverride All/' /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod rewrite
RUN rm -rf /app/*
COPY . /app/
WORKDIR /app
RUN rm Dockerfile
RUN git config --global user.email "michael@easyctf.com"
RUN git config --global user.name "Michael"
RUN git init
RUN echo "easyctf{hiding_the_problem_doesn't_mean_it's_gone!}" > flag.txt
RUN git add . -A
RUN git commit -m "Initial."
RUN git rm flag.txt
RUN git commit -m "Whoops! Remove flag."
RUN echo "Options -Indexes\n" > .htaccess
RUN git add .htaccess
RUN git commit -m "Prevent directory listing."
CMD '/run.sh'