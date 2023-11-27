# Remote Control via Email Command

This is a group project of CSC10008_22CLC02 HCMUS

## Features

__Mail Subject:__ _Remote Control Command_

__Available Commands:__

0. `help` - View Command list
1. `list_apps` - View running applications
2. `list_processes` - View all processes
3. `kill_process <pid>` - Kill process with matching pid
4. `screenshot` - Take a screenshot
5. `webcam` - Take a picture using built-in webcam
6. `keylog <duration>` - Perform keylog for an amount of time
7. `shutdown` - Turn off computer

## Requirements

- [Python 3.10 or newer](https://www.python.org/downloads/)
- __OS__ : Windows
- __Libraries:__

  _- pynput_

  _- psutil_

  _- opencv-python_

  _- packaging_

  _- customtkinter_

**For first time run:** run _setup/setup.bat_ to install necessary packages

## NOTE

_Please allow keylogr.py on Windows Security settings as the system automatically detects this file as a threat_
