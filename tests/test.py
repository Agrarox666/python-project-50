import os.path

from gendiff.scripts.gendiff import generate_diff
from pathlib import Path
def test_gendiff():

    file_path1 = 'fixtures/file1.json'
    file_path2 = 'fixtures/file2.json'
    file_path_expected = 'fixtures/expected1.txt'

    print(open(file_path_expected).read())
    print(generate_diff(file_path1, file_path2))
    assert generate_diff(file_path1, file_path2) == (open(file_path_expected).read())
