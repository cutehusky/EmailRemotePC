import subprocess
import os


def run(cmd):
    os.system(cmd)


def runWithOutput(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)


def getProcessesInfo():
    return runWithOutput('powershell "Get-Process"')


def getAppInfo():
    return runWithOutput(
        'powershell "Get-Process | where-object {$_.MainWindowTitle }"')


def killProcesses(pid):
    run('powershell "Stop-Process -Force -Id ' + str(pid) + '"')


def shutdown():
    run("shutdown /s /t 1")


def logout():
    run("shutdown -l")
