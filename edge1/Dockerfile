FROM tutum/lamp:latest
RUN apt-get update && apt-get install -y git
EXPOSE 80
RUN a2enmod rewrite
RUN rm -rf /app/*
COPY . /app/
WORKDIR /app
RUN rm Dockerfile
RUN git config --global user.email "michael@easyctf.com"
RUN git config --global user.name "Michael"
RUN git init
RUN echo "easyctf{w3_ev3n_u53_git}" >> flag.txt
RUN git add . -A
RUN git commit -m "Initial."
RUN git rm flag.txt
RUN git commit -m "Whoops! Remove flag."
CMD '/run.sh'