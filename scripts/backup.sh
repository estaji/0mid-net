#!/bin/bash

############################################
#Description:	Backup 0mid server files
############################################

# variables
DATE_AND_TIME=$(date +%F-%H-%M-%S)
SYSLOG_FACILITY_NAME=local0.info
LOGGER_TAG=backup-script

# functions
dump_dockerized_mariadb() {
    docker exec mariadb bash -c 'mariadb-dump -u$SITE_DB_USER -p$SITE_DB_PASSWORD $SITE_DB_NAME' > $SITE_DB_NAME-$DATE_AND_TIME.sql
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Dumping database failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Database dumped successfully."
}
backup_nginx_configs() {
    tar -zcf nginx-configs-$DATE_AND_TIME.tar.gz -C / etc/nginx/sites-available etc/nginx/nginx.conf etc/nginx/conf.d
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Nginx backuping failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Nginx configurations backup successfully."
}
archive_website_static_files() {
    tar -czf website_static_and_media-$DATE_AND_TIME.tar.gz -C / var/www/web_media var/www/web_static
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Archive website static and media files failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Website static and media files archived successfully."
}
compress_all() {
    tar --remove-files -czf backup-$DATE_AND_TIME.tar.gz *$DATE_AND_TIME*
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Compressing files failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Files are compressed in one file successfully."
}
backup_monitoring() {
    tar -czf monitoring-stack-$DATE_AND_TIME.tar.gz -C / home/omid/monitoring-dockerized/docker-compose.yaml home/omid/monitoring-dockerized/alertmanager/config home/omid/monitoring-dockerized/prometheus/prometheus.yml home/omid/monitoring-dockerized/prometheus/rules
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Backup monitoring-stack files failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Monitoring-stack files backuped successfully."
}
# main
logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "######## Backup script started ########"
dump_dockerized_mariadb
backup_nginx_configs
archive_website_static_files
backup_monitoring
compress_all
logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "######## Backup script finished ########"
