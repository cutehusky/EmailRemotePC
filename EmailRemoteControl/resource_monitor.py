import psutil
from subprocess import check_output


def list_processes():
    process_list = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
        process_list.append([process.info['pid'], '_'.join(process.info['name'].split()), process.info['status']])
        # return string
    process_list.sort(key= lambda x: x[1])
    formatted_data = """pid name status
------
"""
    for process in process_list:
        formatted_data += f"{process[0]} {process[1]} {process[2]}\n"
    return formatted_data

def kill_process(cmd):
    pid = int(cmd.split()[1])
    process = psutil.Process(pid)
    process.kill()
    print(f'Process {pid} killed')


def getAppInfo():
    return check_output('powershell "Get-Process | where-object {$_.MainWindowTitle }"', shell=True, text=True)


def main():
    processes = list_processes()
    print(processes)
    appinfo = getAppInfo()
    print(appinfo)
if __name__ == "__main__":
    main()
