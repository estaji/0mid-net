#!/bin/bash
# create a tar.gz backup including files, database and nginx config, then upload it to a ftp server
# backup_ftp.sh is here: https://github.com/estaji/useful-bash-scripts

cp /etc/nginx/sites-available/0midnet /home/omid/0midnet/django-personal-website/nginx-config-backup

docker exec mariadb-docker /usr/bin/mysqldump -u root 0middb > /home/omid/0midnet/django-personal-website/database-backup.sql

bash /home/omid/backups/backup_ftp.sh -d /home/omid/0midnet/django-personal-website/ -o /home/omid/backups/temp/bkp-$(date '+%Y-%m-%d-%H-%M-%S').tar.gz -u b110973 -f b110973.parspack.org -p MYPASSWORD

rm -f /home/omid/0midnet/django-personal-website/database-backup.sql
rm -f /home/omid/0midnet/django-personal-website/nginx-config-backup
