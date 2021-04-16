import json


def json_parse(file_path):
    with open(file_path, "r") as file:
        pySchedule = json.load(file)                     # Загружаем json файл и преобразуем в объект python

    print(pySchedule)
    return get_values(pySchedule)


def get_values(json_obj, _list=[]):
    if type(json_obj) is dict:
        for key, value in json_obj.items():
            get_values(value, _list)
    elif type(json_obj) is list:
        for item in json_obj:
            get_values(item, _list)
    else:
        _list.append(json_obj)
    return _list


