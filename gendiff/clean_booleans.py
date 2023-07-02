def format_bool_from_Python_to_Json(_dict):
    for key in _dict:
        if isinstance(_dict[key], dict):
            format_bool_from_Python_to_Json(_dict[key])
        else:
            if _dict[key] is True:
                _dict[key] = 'true'
            elif _dict[key] is False:
                _dict[key] = 'false'
            elif _dict[key] is None:
                _dict[key] = 'null'


def format_bool_from_Json_to_Python(_dict):
    for key in _dict:
        if isinstance(_dict[key], dict):
            format_bool_from_Json_to_Python(_dict[key])
        else:
            if _dict[key] == 'true':
                _dict[key] = True
            elif _dict[key] == 'false':
                _dict[key] = False
            elif _dict[key] == 'null':
                _dict[key] = None
