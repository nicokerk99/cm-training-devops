from functools import cache


def fibonacci(n: int) -> int:
    """Very naive implementation of the Fibonacci sequence where
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1.

    Parameters
    ----------
    n: int
        Index for the number in the Fibonacci sequence, such that fibonacci(n) returns
        the nth number in the series.

    Returns
    ----------
    int
        1 for n = 0
        1 for n = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1

    For n=0 and n=1, returns 1.
    """
    if n < 0:
        raise ValueError(f"Invalid value: n should be >= 0 but was {n}")
    elif n in (0, 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_cached(n: int) -> int:
    """Cached version of the very naive implementation of the Fibonacci sequence where
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1. The caching causes a
    significant performance boost.

    Parameters
    ----------
    n: int
        Index for the number in the Fibonacci sequence, such that fibonacci(n) returns
        the nth number in the series.

    Returns
    ----------
    int
        1 for n = 0
        1 for n = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1

    For n=0 and n=1, returns 1.
    """
    if n < 0:
        raise ValueError(f"Invalid value: n should be >= 0 but was {n}")
    elif n in (0, 1):
        return 1
    else:
        return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
