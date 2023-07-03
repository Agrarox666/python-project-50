### Hexlet tests and linter status:
[![Actions Status](https://github.com/Agrarox666/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Agrarox666/python-project-50/actions) [![CI](https://github.com/Agrarox666/python-project-50/actions/workflows/test.yml/badge.svg)](https://github.com/Agrarox666/python-project-50/actions/workflows/test.yml) <a href="https://codeclimate.com/github/Agrarox666/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/fc1464fbf627ca6f83e8/maintainability" /></a> [![Test Coverage](https://api.codeclimate.com/v1/badges/ab942f403a5d0e3197b6/test_coverage)](https://codeclimate.com/github/Agrarox666/python-project-50/test_coverage)

This is CLI utility to find diff between 2 files

Requirements:
python = "^3.10"
argparse = "^1.4.0"
flake8 = "^6.0.0"
pytest = "^7.3.1"
pytest-cov = "^4.1.0"
pyyaml = "^6.0"

How to install:

Write the commands below in command line:

    1. git clone git@github.com:Agrarox666/python-project-50.git
    2. make package-install
    3. make build
    4. make install

Now you can use the programm.

Usage:
gendiff [-h] [-f FORMAT] first_file second_file
Available formats:

1. stylish - shows tree-diff
2. plain - shows plain-diff (the list of changes)
3. json - shows the diff in json-style 



Examples of using the program:
[![asciicast](https://asciinema.org/a/kpGrv2V7ayxKShbqBzeYPng6U.svg)](https://asciinema.org/a/kpGrv2V7ayxKShbqBzeYPng6U)

[![asciicast](https://asciinema.org/a/Lmc7YiJMkjzZv6N7IyAKruQcP.svg)](https://asciinema.org/a/Lmc7YiJMkjzZv6N7IyAKruQcP)

[![asciicast](https://asciinema.org/a/CVAWg0T7UQlN5BnCRj9GOfckG.svg)](https://asciinema.org/a/CVAWg0T7UQlN5BnCRj9GOfckG)
