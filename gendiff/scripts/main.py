from gendiff_1.cli import get_cli_arguments
from gendiff_1.scripts.gendiff import generate_diff


def main():
    print(generate_diff(*get_cli_arguments()))


if __name__ == '__main__':
    main()
