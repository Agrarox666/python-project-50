import json

from gendiff_project.clean_booleans import format_bool_from_Json_to_Python


def json_formatter(diff):
    def walk(node):

        new_diff = {}
        for key in node:

            if isinstance(node[key], dict):
                new_diff[key.strip()] = walk(node[key])
            else:
                new_diff[key.strip()] = node[key]

        return new_diff

    format_bool_from_Json_to_Python(diff)
    json_diff = json.dumps(walk(diff), indent=2)

    return json_diff
