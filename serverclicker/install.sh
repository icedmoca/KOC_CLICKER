#!/bin/bash

# Update Message of the Day (MOTD)
sudo tee /etc/motd > /dev/null <<-'EOF'
_  ___                      __    _____ _ _      _        
 | |/ (_)                    / _|  / ____| (_)    | |       
 | ' / _ _ __   __ _    ___ | |_  | |    | |_  ___| | _____ 
 |  < | | '_ \ / _` |  / _ \|  _| | |    | | |/ __| |/ / __|
 | . \| | | | | (_| | | (_) | |   | |____| | | (__|   <\__ \
 |_|\_\_|_| |_|\__, |  \___/|_|    \_____|_|_|\___|_|\_\___/
                __/ |                                       
               |___/                                         
-------------------------------------------------------------
-  See whats running:       ps -fA | grep python            -
-  End all the tasks:       sudo pkill python               -
-------------------------------------------------------------
EOF

# Update and install necessary packages
sudo apt-get update --fix-missing
sudo apt-get install -y libappindicator1 fonts-liberation
sudo apt-get install -f
sudo apt-get install -y google-chrome-stable python3 python3-pip python3-selenium

# Install Python packages
pip3 install chromedriver-py selenium-wire mitmproxy

echo "Script installed"
