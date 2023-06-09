from gendiff.scripts.gendiff import generate_diff
def test_gendiff():

    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    file_path_expected = 'tests/fixtures/expected1.txt'

    assert generate_diff(file_path1, file_path2) == (open(file_path_expected).read())
