import pytest

from tests.conftest import run_test

test_lengths = [8, 13, 34, 55, 89, 144, 72, None]


@pytest.mark.parametrize("length", test_lengths)
def test_formatting(manager, length):
    file = "test_files/test_file.rst"
    with open(file) as f:
        test_string = f.read()
    run_test(manager, file, length, test_string)


@pytest.mark.parametrize("length", test_lengths)
def test_bad_table(manager, length):
    file = "test_files/bad_table.rst"
    with open(file) as f:
        test_string = f.read()
    with pytest.raises(NotImplementedError):
        run_test(manager, file, length, test_string)


@pytest.mark.parametrize("length", test_lengths)
def test_errors(manager, length):
    file = "test_files/test_errors.rst"
    with open(file) as f:
        test_string = f.read()
    run_test(manager, file, length, test_string)
