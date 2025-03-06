#!/bin/bash

######################################################
#Description:	Upload a give backup to a minio bucket
######################################################

# variables
BACKUP_FILE=$1
SYSLOG_FACILITY_NAME=local0.info
LOGGER_TAG=backup-archiver
BACKUPS_DIR=/opt/backups
MC_ALIAS=myminio
MC_BUCKET=mybucket
MC_BINARY_PATH=/opt/mc-binary
BKP_OLD_DATE=$(date --iso -d '7 days ago')

# functions
function check_connection {
	$MC_BINARY_PATH/mc ls $MC_ALIAS/$MC_BUCKET/	
	if [ $? -ne 0 ]; then
		logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: $MC_BUCKET is not reachable, connection FAILED!"
		exit 1
	fi
	logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "$MC_BUCKET is reachable."
}
function ensure_backup_exists {
	find $BACKUPS_DIR -type f -name $BACKUP_FILE | grep .
	if [ $? -ne 0 ]; then
        logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Error: The backup file not found!"
        exit 1
    fi
	logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "The backup file exists."
}
function remove_old_backups_locally {
	rm -rfv $BACKUPS_DIR/backup-$BKP_OLD_DATE.tar.gz
	logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Backup $BKP_OLD_DATE was removed locally."
}
function remove_old_backups_remotely {
	$MC_BINARY_PATH/mc rm --recursive --force $MC_ALIAS/$MC_BUCKET/backup-$BKP_OLD_DATE.tar.gz
	logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "Backup $BKP_OLD_DATE was removed from $MC_ALIAS/$MC_BUCKET ."
}
function upload_latest_backup {
	$MC_BINARY_PATH/mc cp --recursive $BACKUPS_DIR/$BACKUP_FILE $MC_ALIAS/$MC_BUCKET/
	logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "$BACKUP_FILE uploaded to $MC_ALIAS/$MC_BUCKET/ successfully."
}

# main
logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "######## Archiving backup started ########"
check_connection
ensure_backup_exists
remove_old_backups_locally
remove_old_backups_remotely
upload_latest_backup
logger -p $SYSLOG_FACILITY_NAME -t "$LOGGER_TAG" "######## Archiving backup finished ########"