import psutil


def list_processes():
    process_list = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
        process_list.append(process.info)
        # return string
    process_list.sort(key=lambda x: x['name'])
    formatted_strings = []
    formatted_strings.append(f'Total number of processes: {len(process_list)}')
    for process in process_list:
        formatted_string = f'pid: {process["pid"]} | name: {process["name"]} | status: {process["status"]}'
        formatted_strings.append(formatted_string)
    return "\n".join(formatted_strings)


def kill_process(pid):
    process = psutil.Process(pid)
    process.kill()
    print(f'Process {pid} killed')
