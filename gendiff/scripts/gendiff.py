from gendiff import generate_diff
from gendiff.cli import get_cli_arguments


def main():
    diff = generate_diff(*get_cli_arguments())
    print(diff)
    print(1)


if __name__ == '__main__':
    main()
