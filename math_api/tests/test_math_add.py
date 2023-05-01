from math_api.math import operations


def test_add_positive():
    assert operations.add(1, 86040049) == 86040050


def test_add_t1_negative():
    assert operations.add(-5, 20) == 15


def test_add_t2_negative():
    assert operations.add(5, -20) == -15


def test_add_params_negative():
    assert operations.add(-5, -20) == -25
