#!/bin/bash

# --settings= is config.settings.production OR config.settings.local
docker exec web python manage.py daemon --settings=config.settings.production