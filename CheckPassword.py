import json


def load(filename):
    file = open(filename)
    data = json.load(file)
    file.close()
    return data


def checkPassword(datas, username, password):
    if username in datas and datas[username] == password:
        return True
    return False
