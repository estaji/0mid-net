#!/bin/bash
timestamp=$(date +%F-%H%M%S)
echo --- backup started at $timestamp ---

echo dumping database...
docker exec mariadb bash -c 'mariadb-dump -u$SITE_DB_USER -p$SITE_DB_PASSWORD $SITE_DB_NAME' > $SITE_DB_NAME-$timestamp.sql

echo nginx config backup is creating...
cp /etc/nginx/sites-available/0mid.net ./0mid.net-nginx-$timestamp

echo media and static files are archiving...
tar -czf web_media-$timestamp.tar.gz /var/www/web_media
tar -czf web_static-$timestamp.tar.gz /var/www/web_static

echo "put all files in a .tar.gz file..."
tar -czf backup-$timestamp.tar.gz *$timestamp*
rm 0middb-$timestamp.sql 0mid.net-nginx-$timestamp web_media-$timestamp.tar.gz web_static-$timestamp.tar.gz

printf "\n--- backup finished ---\n"
