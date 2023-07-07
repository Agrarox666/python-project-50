from gendiff.diff_creator import create_diff
from gendiff.formatters.json_formatter import json_formatter
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.stylish_formatter import stylish


def select_formats(file1, file2, formatter):
    if formatter == 'stylish':
        return stylish(create_diff(file1, file2))
    elif formatter == 'plain':
        return plain(create_diff(file1, file2))
    elif formatter == 'json':
        return json_formatter(create_diff(file1, file2))
    else:
        raise Exception('Unknown format. Available formats are:'
                        ' stylish(default), plain, json')
