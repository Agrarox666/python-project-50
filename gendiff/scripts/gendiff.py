from gendiff import generate_diff
from gendiff.cli import get_cli_arguments


def main():
    arguments = list(get_cli_arguments())
    if arguments[2] is None:
        arguments[2] = 'stylish'
    diff = generate_diff(*arguments)
    print(diff)


if __name__ == '__main__':
    main()
