#!/bin/bash

echo "Checking if Nginx is installed..."
if ! command -v sudo nginx &> /dev/null
then
    echo "Nginx is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y nginx
else
    echo "Nginx is already installed."
fi

echo "Checking if Supervisor is installed..."
if ! command -v supervisorctl &> /dev/null
then
    echo "Supervisor is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y supervisor
else
    echo "Supervisor is already installed."
fi

echo "Checking if Python 3 is installed..."
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y python3
else
    echo "Python 3 is already installed."
fi


echo "Checking if pip3 is installed..."
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y python3-pip
else
    echo "pip3 is already installed."
fi

echo "Checking if Python virtual environment is installed..."
if ! dpkg -s python3-venv &> /dev/null
then
    echo "Python virtual environment is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y python3-venv
else
    echo "Python virtual environment is already installed."
fi

echo "Checking if Git is installed..."
if ! command -v git &> /dev/null
then
    echo "Git is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y git
else
    echo "Git is already installed."
fi

echo "Installation complete."
echo "Nginx version: $(sudo nginx -v 2>&1 | grep -oP '(?<=nginx\/)[0-9]+\.[0-9]+\.[0-9]+')"
echo "Supervisor version: $(supervisord -v)"
echo "Python 3 version: $(python3 --version | cut -d ' ' -f 2)"
echo "Git version: $(git --version | cut -d ' ' -f 3)"
