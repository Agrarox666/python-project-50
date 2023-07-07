import json

from gendiff.booleans_cleaner import format_bool_from_json_to_python


def json_formatter(diff):
    def walk(node):

        new_diff = {}
        for key in node:

            if isinstance(node[key], dict):
                new_diff[key.strip()] = walk(node[key])
            else:
                new_diff[key.strip()] = node[key]

        return new_diff

    format_bool_from_json_to_python(diff)
    json_diff = json.dumps(walk(diff), indent=2)

    return json_diff
