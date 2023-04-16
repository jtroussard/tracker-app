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
sudo mkdir -p /home/jacques_troussard/logs
logfile="/home/jacques_troussard/logs/tracker-app.deploy_$(date +"%Y%m%d%H%M%S%3N").log"

# Redirect all output to the log file
exec &> >(tee -a "$logfile")

# Check if there is a newer release available
latest_tag=$(git describe --tags --abbrev=0 origin/61-feature-create-release-and-deploy-script)
current_tag=$(git describe --tags)
echo "latest_tag: $latest_tag"
echo "current_tag: $current_tag"
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
git checkout $latest_tag || {
    echo "Failed to checkout latest release. Rolling back..."
    git checkout $current_tag
    rm -rf /home/jacques_troussard/service/tracker-app
    cp -r ../backup/* .
    exit 1
}

# Copy the project to the specified directory
mkdir -p /home/jacques_troussard/service/tracker-app
cp -r \
./LICENSE \
./run.py \
./weight_tracker \
./requirements.txt \
-t /home/jacques_troussard/service/tracker-app || {
    echo "Failed to copy project to specified directory. Rolling back..."
    git checkout $current_tag
    rm -rf /home/jacques_troussard/service/tracker-app
    cp -r ../backup/* .
    exit 1
}

# Change into the service directory
cd /home/jacques_troussard/service/tracker-app || {
    echo "Failed to change into service directory. Rolling back..."
    git checkout $current_tag
    rm -rf /home/jacques_troussard/service/tracker-app
    cp -r ../backup/* .
    exit 1
}

# Install dependencies
python3 -m venv venv || {
    echo "Failed to create virtual environment. Rolling back..."
    git checkout $current_tag
    rm -rf /home/jacques_troussard/service/tracker-app
    cp -r ../backup/* .
    exit 1
}
source venv/bin/activate || {
    echo "Failed to activate virtual environment. Rolling back..."
    git checkout $current_tag
    rm -rf /home/jacques_troussard/service/tracker-app
    cp -r ../backup/* .
    exit 1
}
pip install -r requirements.txt || {
    echo "Failed to install dependencies. Rolling back..."
    git checkout $current_tag
    rm -rf /home/jacques_troussard/service/tracker-app
    cp -r ../backup/*
}

# NGINX
# Check if Nginx config file has changed
if [ -f /config/trackerapp.devlife4.me-nginx.conf ]; then
    if [ $(diff /etc/nginx/sites-enabled/trackerapp.devlife4.me-nginx.conf /home/jacques_troussard/service/trackerapp/weight_tracker_2/config/trackerapp.devlive4.me-nginx.conf | wc -l) -ne 0 ]; then
        # Reload Nginx configuration
        if ! sudo nginx -t && sudo nginx -s reload; then
            echo "Failed to reload Nginx configuration. Rolling back..."
            git checkout $current_tag
            cp -r ../backup/* .
            exit 1
        fi

        # Restart Nginx server
        if ! sudo systemctl restart nginx; then
            echo "Failed to restart Nginx server. Rolling back..."
            git checkout $current_tag
            cp -r ../backup/* .
            exit 1
        fi
    fi
fi

# Reread the Supervisor configuration file
if ! sudo supervisorctl reread; then
    echo "Failed to reread the Supervisor configuration file. Rolling back..."
    git checkout $current_tag
    cp -r ../backup/* .
    exit 1
fi

# Restart Supervisor to reload the app
if ! sudo supervisorctl restart weight-tracker-2; then
    echo "Failed to restart app with Supervisor. Rolling back..."
    git checkout $current_tag
    cp -r ../backup/* .
    exit 1
fi

# Turn off the redirect and echo to the screen
exec &> /dev/tty
echo "Deployment completed successfully"