From python:3.10-alpine

LABEL maintainer="Omid Estaji <estaji.work@gmail.com>"
LABEL project="0mid-net-website"

ENV TZ=Asia/Tehran
ENV APP_USER=website
ENV SITE_SECRET_KEY=mycomplexstring
ENV SITE_DB_NAME=mydb
ENV SITE_DB_USER=myuser
ENV SITE_DB_PASSWORD=mypass
ENV SITE_DB_HOST=127.0.0.1
ENV SITE_DB_PORT=3306
ENV SITE_ENV=production

EXPOSE 8080

WORKDIR /opt/app

COPY ../django/requirements/ ./requirements

RUN apk update && apk add gcc musl-dev mariadb-connector-c-dev
RUN pip install -U pip
RUN pip install -r requirements/production.txt

VOLUME /opt/app/media
VOLUME /opt/app/static_root

COPY ../django/ .

RUN addgroup --system --gid 1010 $APP_USER
RUN adduser --system --uid 1010 $APP_USER

RUN chown -R $APP_USER:$APP_USER /opt/app

USER $APP_USER

ENTRYPOINT ["gunicorn"]

CMD ["-c", "gunicorn.conf.py"]

ARG GIT_BRANCH=None GIT_TAG=None GIT_COMMIT=None
LABEL GIT_BRANCH=$GIT_BRANCH GIT_TAG=$GIT_TAG GIT_COMMIT=$GIT_COMMIT

ARG BUILD_TAG=None BUILD_ID=None
LABEL BUILD_TAG=$BUILD_TAG BUILD_ID=$BUILD_ID