from fastapi import APIRouter

from math_api.math import fibonacci, operations

router = APIRouter()


@router.get("/health")
def health() -> str:
    return "I'm alive!"


@router.get("/add")
def add(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1+t2."""
    return operations.add(t1, t2)


@router.get("/sub")
def sub(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1-t2."""
    return operations.sub(t1, t2)


@router.get("/div")
def div(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1/t2."""
    return operations.div(t1, t2)


@router.get("/mul")
def mul(t1: int, t2: int) -> int:
    """For two integers t1 and t2, returns t1*t2."""
    return operations.mul(t1, t2)


@router.get("/fib")
def fib(n: int) -> int:
    """Returns the nth number in the fibonacci series."""
    return fibonacci.fibonacci(n)


@router.get("/fib_cache")
def fib_cache(n: int) -> int:
    """Returns the nth number in the fibonacci series. Improved performance."""
    return fibonacci.fibonacci_cached(n)
