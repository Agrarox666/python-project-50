from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.gendiff import parser
def test_generate_diff():

    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    file_path_expected = 'tests/fixtures/expected1.txt'

    assert generate_diff(file_path1, file_path2) == (open(file_path_expected).read())

def test_parser():

    file_path1 = 'tests/fixtures/filepath1.yml'
    file_path2 = 'tests/fixtures/filepath2.yml'
    file_path_expected = 'tests/fixtures/expected2.txt'

    assert generate_diff(file_path1, file_path2) == (open(file_path_expected).read())
