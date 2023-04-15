#!/bin/bash

# Deploy script
# 1. Check if there is a newer release available
# 2. If there is a newer release available, copy the contents of the current directory to ../old
# 3. Check out the latest release
# 4. Copy the project to the specified directory
# 5. Change into the service directory
# 6. Install dependencies
# 7. Check if Nginx config file has changed
# 8. Reload Nginx configuration if changed
# 9. Restart Nginx server if configuration was reloaded
# 10. Reread the Supervisor configuration file
# 11. Restart Supervisor to reload the app
# 12. Redirect all output to a log file with a timestamp in the file name

# Set the log file name with a timestamp
sudo mkdir -p /var/log/tracker-app/
logfile="/var/log/tracker-app/tracker-app.deploy_$(date +"%Y%m%d%H%M%S%3N").log"

# Redirect all output to the log file
exec &> >(tee -a "$logfile")

# Check if there is a newer release available
latest_tag=$(git describe --abbrev=0 --tags)
current_tag=$(git describe --tags)
if [ $latest_tag == $current_tag ]; then
    echo "No new release available. Exiting..."
    exit 0
else
    # Copy the contents of the current directory to ../old
    mkdir -p ../backup
    rm -rf ../backup/*
    cp -r ./* ../backup
fi

# Check out the latest release
git checkout $latest_tag

# Copy the project to the specified directory
cp -r \
./LICENSE \
./run.py \
./weight_tracker \
./requirements \
-t /home/jacques_troussard/service

# Change into the service directory
cd /home/jacques_troussard/service/weight_tracker

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Check if Nginx config file has changed
if [ -f /config/trackerapp.devlife4.me-nginx.conf ]; then
    if [ $(diff /etc/nginx/sites-enabled/trackerapp.devlife4.me-nginx.conf /config/trackerapp.devlife4.me-nginx.conf | wc -l) -ne 0 ]; then
        # Reload Nginx configuration
        sudo nginx -t && sudo nginx -s reload

        # Restart Nginx server
        sudo systemctl restart nginx
    fi
fi

# Reread the Supervisor configuration file
sudo supervisorctl reread

# Restart Supervisor to reload the app
sudo supervisorctl restart weight-tracker-2

# Turn off the redirect and echo to the screen
exec &> /dev/tty
echo "Deployment completed successfully"
