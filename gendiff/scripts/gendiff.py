import argparse
import json
import yaml

from gendiff.scripts.plain import plain
from gendiff.scripts.stylish import stylish
from gendiff.scripts.json_formatter import json_formatter


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()


def generate_diff(file_path1, file_path2, formatter='stylish'):
    if file_path1[-5:] == '.json' and file_path2[-5:] == '.json':
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))

    elif file_path1[-4:] == '.yml' and file_path2[-4:] == '.yml':
        file1 = yaml.load(open(file_path1), Loader=yaml.FullLoader)
        file2 = yaml.load(open(file_path2), Loader=yaml.FullLoader)
    else:
        print('Files are in the wrong format')
        return 0

    clean_booleans(file1)
    clean_booleans(file2)
    if formatter == 'stylish':
        return stylish(create_diff(file1, file2))
    elif formatter == 'plain':
        return plain(create_diff(file1, file2))
    elif formatter == 'json':
        return json_formatter(create_diff(file1, file2))


# flake8: noqa: C901
def create_diff(file1: dict, file2: dict):
    def walk(node1: dict, node2: dict, depth=0):

        keys = set(node1.keys())
        keys.update(node2.keys())
        keys = sorted(keys)
        diff = {}

        for key in keys:
            if key in node1 and key in node2:
                if node1[key] == node2[key]:
                    diff[f'{key}'] = node1[key]
                else:
                    if isinstance(node1[key], dict) and \
                            isinstance(node2[key], dict):
                        diff[f'{key}'] = walk(node1[key], node2[key], depth + 1)
                    else:
                        diff[f'- {key}'] = node1[key]
                        diff[f'+ {key}'] = node2[key]
            elif key in node1:
                diff[f' - {key}'] = node1[key]
            else:
                diff[f' + {key}'] = node2[key]
        return diff

    return walk(file1, file2, 1)


def clean_booleans(_dict):
    for key in _dict:
        if isinstance(_dict[key], dict):
            clean_booleans(_dict[key])
        else:
            if _dict[key] is True:
                _dict[key] = 'true'
            elif _dict[key] is False:
                _dict[key] = 'false'
            elif _dict[key] is None:
                _dict[key] = 'null'
