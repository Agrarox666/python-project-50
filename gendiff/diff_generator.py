from gendiff.booleans_cleaner import format_bool_from_python_to_json

from gendiff.data_reader import read_data
from gendiff.data_reader import define_extension
from gendiff.data_loader import recognize
from gendiff.format_selector import select_formats


def generate_diff(file_path1, file_path2, formatter='stylish'):

    file1 = recognize(read_data(file_path1), define_extension(file_path1))
    file2 = recognize(read_data(file_path2), define_extension(file_path2))

    formatted_file1 = format_bool_from_python_to_json(file1)
    formatted_file2 = format_bool_from_python_to_json(file2)

    return select_formats(formatted_file1, formatted_file2, formatter)
