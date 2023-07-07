def format_bool_from_python_to_json(some_dict):
    new_dict = some_dict
    change_type_from_python_to_json(new_dict)
    return new_dict


def format_bool_from_json_to_python(some_dict):
    new_dict = some_dict
    change_type_from_json_to_python(new_dict)
    return new_dict


def change_type_from_python_to_json(_dict):
    for key in _dict:
        if type(_dict[key]) is dict:
            format_bool_from_python_to_json(_dict[key])
        else:
            if _dict[key] is True:
                _dict[key] = 'true'
            elif _dict[key] is False:
                _dict[key] = 'false'
            elif _dict[key] is None:
                _dict[key] = 'null'


def change_type_from_json_to_python(_dict):
    for key in _dict:
        if isinstance(_dict[key], dict):
            format_bool_from_json_to_python(_dict[key])
        else:
            if _dict[key] == 'true':
                _dict[key] = True
            elif _dict[key] == 'false':
                _dict[key] = False
            elif _dict[key] == 'null':
                _dict[key] = None
