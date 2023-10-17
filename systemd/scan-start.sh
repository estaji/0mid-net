#!/bin/bash
cd $SITE_PROJECT_PATH
# --settings= is config.settings.production OR config.settings.local
$SITE_VENV_PATH/venv/bin/python manage.py daemon --settings=config.settings.$SITE_ENV