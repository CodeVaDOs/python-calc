import json
import os


def json_parse(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        pySchedule = json.load(file)  # Загружаем json файл и преобразуем в объект python
    remove_file(file_path)
    print(pySchedule)
    str1 = " "
    return str1.join(get_values(pySchedule, []))


def get_values(json_obj, _list=[]):
    new_row = '\n'
    tabulation = '  '
    if type(json_obj) is dict:
        for key, value in json_obj.items():
            _list.append(new_row)
            get_values(value, _list)
    elif type(json_obj) is list:
        for item in json_obj:
            _list.append(new_row)
            _list.append(tabulation)
            get_values(item, _list)
    else:
        _list.append(json_obj)

    return _list


def remove_file(path):
    print(path)
    os.remove(path)
