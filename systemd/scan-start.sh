#!/bin/bash
cd /home/omid/Projects/0mid.net/0mid.net_project/
# for production use config.settings.production instead of config.settings.local
/home/omid/Projects/0mid.net/my_venv/bin/python manage.py daemon --settings=config.settings.local