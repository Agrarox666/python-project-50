import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.indir)


if __name__ == '__main__':
    main()

def generate_diff(file_path1, file_path2):

    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))

    keys = set(json1.keys())
    keys.update(json2.keys())
    keys = sorted(keys)
    result = '{'

    for key in keys:
        if key in json1 and key in json2:
            if json1[key] == json2[key]:
                result = f'{result}\n   {key}: {json1[key]}'
            else:
                result = f'{result}\n - {key}: {json1[key]}\n + {key}: {json2[key]}'
        elif key in json1:
            result = f'{result}\n - {key}: {json1[key]}'
        else:
            result = f'{result}\n + {key}: {json2[key]}'
    result += '\n}'

    return result