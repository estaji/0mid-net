From python:3.10-alpine

LABEL maintainer="Omid Estaji <estaji.work@gmail.com>"

ENV SITE_SECRET_KEY=mycomplexstring
ENV SITE_DB_NAME=mydb
ENV SITE_DB_USER=myuser
ENV SITE_DB_PASSWORD=mypass
ENV SITE_DB_HOST=127.0.0.1
ENV SITE_DB_PORT=3306
ENV SITE_ENV=production

EXPOSE 8080

WORKDIR /opt/app

COPY requirements/ ./requirements

RUN apk update && apk add gcc musl-dev mariadb-connector-c-dev
RUN pip install -U pip
RUN pip install -r requirements/production.txt

VOLUME /opt/app/media
VOLUME /opt/app/static_root

COPY . .

RUN adduser -DH -g omid omid
RUN chown -R omid:omid /opt/app

USER 1000

ENTRYPOINT ["gunicorn"]

CMD ["-c", "gunicorn.conf.py"]