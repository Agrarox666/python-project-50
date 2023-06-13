import argparse
import json

import yaml


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()


def generate_diff(file_path1, file_path2):

    if file_path1[-5:] == '.json' and file_path2[-5:] == '.json':
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))

    elif file_path1[-4:] == '.yml' and file_path2[-4:] == '.yml':
        file1 = yaml.load(open(file_path1))
        file2 = yaml.load(open(file_path2))
    else:
        print('Files are in the wrong format')
        return 0

    return parser(file1, file2)


def parser(file1, file2):

    keys = set(file1.keys())
    keys.update(file2.keys())
    keys = sorted(keys)

    result = '{'
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result = f'{result}\n    {key}: {file1[key]}'
            else:
                result = f'{result}\n  - {key}: ' \
                         f'{file1[key]}\n  + {key}: {file2[key]}'
        elif key in file1:
            result = f'{result}\n  - {key}: {file1[key]}'
        else:
            result = f'{result}\n  + {key}: {file2[key]}'
    result += '\n}'

    return result
