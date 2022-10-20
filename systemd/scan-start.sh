#!/bin/bash
cd /home/omid/Projects/0mid.net/0mid.net_project/
# for local use config.settings.local instead of config.settings.production
/home/omid/Projects/0mid.net/my_venv/bin/python manage.py daemon --settings=config.settings.production