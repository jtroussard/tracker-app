#!/bin/bash

# Check if APP_NAME is provided as an argument
if [ -z "$1" ]
then
  echo "Please provide APP_NAME as an argument"
  exit 1
fi

BASE_DIR="./test-service"
APP_NAME=$1

PWD=$(pwd)
echo $PWD
echo "$BASE_DIR/$APP_NAME"
# Check if directory exists
if [ -d "$BASE_DIR/$APP_NAME" ]
then
  # Create 'old' directory if it does not exist
  mkdir -p "$BASE_DIR/old/"

  # Copy directory to 'old' directory
  cp -r "$BASE_DIR/$APP_NAME" "$BASE_DIR/old/"

  # Remove directory
  rm -rf "$BASE_DIR/$APP_NAME"

  echo "Directory $APP_NAME has been moved to $BASE_DIRold/"
else
  echo "Directory $APP_NAME does not exist"
fi

# Redirect all output to log file
LOG_FILE="$BASE_DIR/$APP_NAME/tracker-app.deploy_$(date +"%Y%m%d%H%M%S%3N").log"
exec &> >(tee -a "$LOG_FILE")

echo "Logging to $LOG_FILE"
