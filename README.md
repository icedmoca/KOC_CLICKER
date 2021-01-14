# Clicker Installer

This is a simple install script for the instant clicker for the King of Clicks competition.

### System requirements
__CPU: `2+` MEMORY: `4gb+`__ 
Tested on ubuntu 20.04 (Recommended)

_6 instances = `2`cpu `4gb`ram_

_12 instances = `4`cpu `6gb`ram_



## How to install:

1. Install the repo: `git clone https://github.com/icedmoca/clickinstaller.git`
2. Go to directory: `cd clickinstaller`
3. Give permissions: `chmod 777 install.sh`
4. Run installer: `./install.sh`
5. Make sure you are in: `cd clickinstaller`
6. Run: `python3 1.py`

Run multiple: `python3 1.py & python3 1.py & python3 1.py`

## Install on server:
1. `git clone https://github.com/icedmoca/clickinstaller.git && cd clickinstaller && chmod 777 install.sh`
2. `cd clickinstaller && python3 1.py & python3 1.py & python3 1.py & python3 1.py & python3 1.py & python3 1.py`

### To exit script
`CTRL+C` and end all python processes `sudo pkill python` make sure none are running `sudo pgrep python`

###### Dependencies installed
 * python3
 * python3-pip
 * python3-selenium
 * python3-selenium-wire
 * python3-mitmproxy
 * chromedriver-py
 * libappindicator1 
 * fonts-liberation