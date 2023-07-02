from gendiff import generate_diff


def test_generate_diff1():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    file_path_expected = 'tests/fixtures/expected1.txt'

    assert generate_diff(file_path1, file_path2) == (open(file_path_expected).read())


def test_generate_diff2():
    file_path1 = 'tests/fixtures/filepath1.yml'
    file_path2 = 'tests/fixtures/filepath2.yml'
    file_path_expected = 'tests/fixtures/expected2.txt'

    assert generate_diff(file_path1, file_path2) == (open(file_path_expected).read())


def test_deep_diff():
    file_path3 = 'tests/fixtures/file3.json'
    file_path4 = 'tests/fixtures/file4.json'
    file_path_expected = 'tests/fixtures/expected3.txt'
    assert generate_diff(file_path3, file_path4) == (open(file_path_expected).read())


def test_plain_diff():
    file_path3 = 'tests/fixtures/file3.json'
    file_path4 = 'tests/fixtures/file4.json'
    file_path_expected = 'tests/fixtures/expected4.txt'
    assert generate_diff(file_path3, file_path4, 'plain') == (open(file_path_expected).read())


def test_json_diff():
    file_path3 = 'tests/fixtures/file3.json'
    file_path4 = 'tests/fixtures/file4.json'
    file_path_expected = 'tests/fixtures/expected5.json'
    assert generate_diff(file_path3, file_path4, 'json') == (open(file_path_expected).read())
