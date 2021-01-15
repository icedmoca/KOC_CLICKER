#!/bin/bash
sudo bash -c 'cat > /etc/motd' <<-'EOF'
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

sudo apt-get update --fix-missing
sudo apt-get install -y libappindicator1 fonts-liberation
sudo apt-get install -f
sudo apt-get install google-chrome-stable
sudo apt install -y python3
sudo apt install -y python3-pip
sudo apt install -y python3-selenium
pip3 install chromedriver-py
pip3 install selenium-wire
pip3 install mitmproxy
cd /bin
sudo chmod +x chromedriver
mv clickinstaller/1.py clickinstaller/..
