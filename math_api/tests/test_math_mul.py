from math_api.math import operations


def test_mul_positive():
    assert operations.mul(1, 86040049) == 86040049


def test_mul_t1_negative():
    assert operations.mul(-5, 20) == -100


def test_mul_t2_negative():
    assert operations.mul(5, -20) == -100


def test_mul_params_negative():
    assert operations.mul(-5, -20) == 100


def test_mul_by_zero():
    assert operations.mul(1, 0) == 0
