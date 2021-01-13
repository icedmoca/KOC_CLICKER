#!/bin/bash
bash -c 'cat > /etc/motd' <<-'EOF'
_  ___                      __    _____ _ _      _        
 | |/ (_)                    / _|  / ____| (_)    | |       
 | ' / _ _ __   __ _    ___ | |_  | |    | |_  ___| | _____ 
 |  < | | '_ \ / _` |  / _ \|  _| | |    | | |/ __| |/ / __|
 | . \| | | | | (_| | | (_) | |   | |____| | | (__|   <\__ \
 |_|\_\_|_| |_|\__, |  \___/|_|    \_____|_|_|\___|_|\_\___/
                __/ |                                       
               |___/                                         
EOF

apt-get update --fix-missing
apt install -y python3
apt install -y python3-pip
apt install -y python3-selenium
pip3 install chromedriver-py
git clone https://github.com/icedmoca/click.git
cd click
python3 1.py
