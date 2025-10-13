FROM python:3.12-alpine AS builder

RUN apk update \
    && apk add --no-cache \
        gcc \
        musl-dev \
        postgresql-dev \
        python3-dev \
    && pip install -U pip

WORKDIR /opt/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

FROM python:3.12-alpine

LABEL maintainer="Omid Estaji <estaji.work@gmail.com>"
LABEL project="0mid.net"

ENV TZ=Asia/Tehran
ENV APP_USER=website
ENV SITE_SECRET_KEY=mycomplexstring
ENV SITE_DB_NAME=mydb
ENV SITE_DB_USER=myuser
ENV SITE_DB_PASSWORD=mypass
ENV SITE_DB_HOST=127.0.0.1
ENV SITE_DB_PORT=5432
ENV DJANGO_SETTINGS_MODULE=dev

EXPOSE 8080

WORKDIR /opt/app

# Install the Postgres runtime library
RUN apk update \
    && apk add --no-cache libpq \
    && rm -rf /var/cache/apk/*

COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/

COPY . .

RUN addgroup --system --gid 1010 $APP_USER \
    && adduser --system --uid 1010 $APP_USER \
    && chown -R $APP_USER:$APP_USER /opt/app

VOLUME /opt/app/media
VOLUME /opt/app/static_root

USER $APP_USER

ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py"]

ARG GIT_BRANCH=None GIT_TAG=None GIT_COMMIT=None
LABEL GIT_BRANCH=$GIT_BRANCH GIT_TAG=$GIT_TAG GIT_COMMIT=$GIT_COMMIT

ARG BUILD_TAG=None BUILD_ID=None
LABEL BUILD_TAG=$BUILD_TAG BUILD_ID=$BUILD_ID