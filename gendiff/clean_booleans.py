import copy


def format_bool_from_Python_to_Json(_dict):
    new_dict = copy.deepcopy(_dict)
    for key in new_dict:
        if isinstance(new_dict[key], dict):
            return format_bool_from_Python_to_Json(new_dict[key])
        else:
            if new_dict[key] is True:
                new_dict[key] = 'true'
            elif new_dict[key] is False:
                new_dict[key] = 'false'
            elif new_dict[key] is None:
                new_dict[key] = 'null'
    return format_bool_from_Python_to_Json(new_dict)


def format_bool_from_Json_to_Python(_dict):
    new_dict = copy.deepcopy(_dict)
    for key in new_dict:
        if isinstance(new_dict[key], dict):
            return format_bool_from_Json_to_Python(new_dict[key])
        else:
            if new_dict[key] == 'true':
                new_dict[key] = True
            elif new_dict[key] == 'false':
                new_dict[key] = False
            elif new_dict[key] == 'null':
                new_dict[key] = None
    return format_bool_from_Json_to_Python(new_dict)