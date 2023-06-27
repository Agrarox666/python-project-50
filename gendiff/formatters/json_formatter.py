import json


def json_formatter(diff):
    def walk(node):

        new_diff = {}
        for key in node:

            if isinstance(node[key], dict):
                new_diff[key.strip()] = walk(node[key])
            else:
                new_diff[key.strip()] = node[key]

        return new_diff

    clean_booleans(diff)
    json_diff = json.dumps(walk(diff), indent=2)

    return json_diff


def clean_booleans(_dict):
    for key in _dict:
        if isinstance(_dict[key], dict):
            clean_booleans(_dict[key])
        else:
            if _dict[key] == 'true':
                _dict[key] = True
            elif _dict[key] == 'false':
                _dict[key] = False
            elif _dict[key] == 'null':
                _dict[key] = None
