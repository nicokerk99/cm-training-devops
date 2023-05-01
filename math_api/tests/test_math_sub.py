from math_api.math import operations


def test_sub_positive():
    assert operations.sub(1, 86040049) == -86040048


def test_sub_t1_negative():
    assert operations.sub(-5, 20) == -25


def test_sub_t2_negative():
    assert operations.sub(5, -20) == 25


def test_sub_params_negative():
    assert operations.sub(-5, -20) == 15
