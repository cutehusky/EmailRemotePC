# Remote Control via Email Command

This is a group project of CSC10008_22CLC02 HCMUS

## Features

__Default Recipient Email:__ dummymailbox5186@gmail.com

_You can use yours instead by making change in resource/variables.py. Please note that it requires **App password** and NOT your account password._

[[How to get app password]](https://support.google.com/mail/answer/185833?hl=en)

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

_Please exclude this folder from Windows Defender scans as the system automatically detects **resource/keylogr.py** as a threat_
**[Instruction](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26#:~:text=Go%20to%20Start%20>%20Settings%20>%20Update,%2C%20file%20types%2C%20or%20process.)**