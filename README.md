## About

This command line based tool on Linux is designed to quickly and easily install, update, remove astra software and install the TBS driver without copying and pasting long commands from astra website files.

## Features

- ✅ Check license
- ✅ Install astra
- ✅ Update astra
- ✅ Remove astra
- ✅ TBS driver installation

❗ Working only debian based **Linux system** and **root** access (for example ubuntu, kali, debian, and etc...)

## How to run tool

1. To install the tool, you need to install python3 on your system if it is not installed, for this, type in the terminal `sudo apt install python3 -y` this command installs the python3 tool to work.
2. You need to create an environment variable on your Linux system and install the astra license and then run the program with sudo -E (root is supposed to take the current user's environment variable) and python3 astra.py is supposed to run with python3 our program as root

```
ASTRA_LICENCE=license_key
sudo -E python3 astra.py
```
### You should see the following menu

```
usage: astra.py [-h] [-up] [-i] [-r] [-tdi]

Astra control cli based tool

options:
  -h, --help            show this help message and exit
  -up, --update         Update astra
  -i, --install         Install astra
  -r, --remove          Remove astra
  -tdi, --tbs_driver_install
                        Installing TBS driver
```

Usage examples

`sudo python astra.py -i`
Install Astra

`sudo python astra.py -up`
Update Astra

`sudo python astra.py -r`
Remove Asrea

`sudo python astra.py -tdi`
TBS driver installation

License need only install astra, not needed license for uninstall, update or TBS driver installation

[Astra official document](https://help.cesbo.com/)
