import json

import yaml
from gendiff.cli import get_cli_arguments

from gendiff.create_diff import create_diff

from gendiff.clean_booleans import format_bool_from_Python_to_Json
from gendiff.formatters.json_formatter import json_formatter
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.stylish_formatter import stylish


def generate_diff(file_path1, file_path2, formatter='stylish'):
    if file_path1.endswith('.json') and file_path2.endswith('.json'):
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))

    elif file_path1.endswith('.yml') and file_path2.endswith('.yml'):
        file1 = yaml.load(open(file_path1), Loader=yaml.FullLoader)
        file2 = yaml.load(open(file_path2), Loader=yaml.FullLoader)
    else:
        raise Exception

    format_bool_from_Python_to_Json(file1)
    format_bool_from_Python_to_Json(file2)
    if formatter == 'stylish':
        return stylish(create_diff(file1, file2))
    elif formatter == 'plain':
        return plain(create_diff(file1, file2))
    elif formatter == 'json':
        return json_formatter(create_diff(file1, file2))


def main():
    print(generate_diff(*get_cli_arguments()))


if __name__ == '__main__':
    print(generate_diff(*get_cli_arguments()))
