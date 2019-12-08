#!/bin/sh

# Simplifies the environment setup so that the code can be
# executed immediately on a new machine.

env_location=$1
if [ -z "$1" ]; then
    env_location="/tmp/rrt_virtualenv"
fi

# ensure the virtual environment's location exists
if [ ! -d "$env_location" ]; then
    while true; do
        read -p "Virtual Environment location $env_location does not exist. Do you want to create it? [y/n]: " yn
        case $yn in
            [Yy]* ) mkdir -p $env_location; break;;
            [Nn]* ) echo "Exiting setup"; exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
fi

# ensure the thing at the location is actually a virtual environment
if [ ! -f "$env_location/pyvenv.cfg" ]; then 
    while true; do
        read -p "$env_location does not yet contain a virtual environment. Create one? [y/n]: " yn
        case $yn in
            [Yy]* ) sudo apt-get install python3-venv; python3 -m venv $env_location; break;;
            [Nn]* ) echo "Exiting setup"; exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
fi

# ensure the environment has the required dependencies
. $env_location/bin/activate
pip install -r requirements.txt | grep -v 'already satisfied'

chmod +x ./main.py
./main.py