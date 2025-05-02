#!/bin/bash

############################################
#Description:	Backup 0mid server files
############################################

# variables
DATE_AND_TIME=$(date --iso)
SYSLOG_FACILITY_NAME=local0.info
LOGGER_TAG=backup-script
WEBSITE_DB_CONTAINER=0mid-net-mariadb
DOCKER_COMPOSE_ENV_FILE_PATH=opt/0mid-net-website/docker/.env
ARCHIVER_SCRIPT=/opt/backups/backup-archiver.sh
BACKUPS_DIR=/opt/backups/

# functions
dump_dockerized_mariadb() {
    docker exec $WEBSITE_DB_CONTAINER bash -c 'mariadb-dump -u$SITE_DB_USER -p$SITE_DB_PASSWORD $SITE_DB_NAME' > website-database-$DATE_AND_TIME.dump
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
backup_monitoring() {
    tar -czf monitoring-stack-$DATE_AND_TIME.tar.gz -C / opt/monitoring-stack/docker-compose.yaml opt/monitoring-stack/alertmanager/config opt/monitoring-stack/prometheus/prometheus.yml opt/monitoring-stack/prometheus/rules
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Backup monitoring-stack files failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Monitoring-stack files backuped successfully."
}
backup_3xui() {
    tar -czf 3x-ui-$DATE_AND_TIME.tar.gz -C / opt/3x-ui/docker-compose.yaml opt/3x-ui/db/ opt/3x-ui/letsencrypt/
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Backup 3x-ui files failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "3x-ui files backuped successfully."

}
backup_firewall() {
    tar -czf firewall-$DATE_AND_TIME.tar.gz -C / /etc/iptables/rules.v4
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Backup firewall file failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "firewall file backuped successfully."

}
backup_envs() {
    tar -czf environment-variables-$DATE_AND_TIME.tar.gz -C / $DOCKER_COMPOSE_ENV_FILE_PATH
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Backup environment-variables file failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "environment-variables file backuped successfully."

}
compress_all() {
    tar --remove-files -czf backup-$DATE_AND_TIME.tar.gz *$DATE_AND_TIME*
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Compressing files failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Files are compressed in one file successfully."
}
archive_backup() {
    cd $BACKUPS_DIR
    bash $ARCHIVER_SCRIPT backup-$DATE_AND_TIME.tar.gz
    if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: Archiving backup failed!"
    fi
    logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Archiving script executed successfully."
}

# main
logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "######## Backup script started ########"
dump_dockerized_mariadb
backup_nginx_configs
archive_website_static_files
backup_monitoring
backup_envs
backup_3xui
backup_firewall
compress_all
archive_backup
logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "######## Backup script finished ########"
