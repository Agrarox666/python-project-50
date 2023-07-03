from gendiff.clean_booleans import format_bool_from_Python_to_Json

from gendiff.get_data import get_data_from_file
from gendiff.recognize import recognize
from gendiff.formats import select_formats


def generate_diff(file_path1, file_path2, formatter='stylish'):

    file1 = recognize(*get_data_from_file(file_path1))
    file2 = recognize(*get_data_from_file(file_path2))

    format_bool_from_Python_to_Json(file1)
    format_bool_from_Python_to_Json(file2)

    return select_formats(file1, file2, formatter)
