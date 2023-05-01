# Python 301

In this exercise, you will implement a calculator API that serves endpoints for mathematical functions using [FastAPI](https://fastapi.tiangolo.com/). The goal is to make you familiar with building APIs, [`poetry`](https://python-poetry.org/) for package and dependency management and [`pytest`](https://pytest.org) for testing. You should also make sure that your code is properly formatted using [`black`](https://github.com/psf/black) and [`isort`](https://pycqa.github.io/isort/).


## Getting started

1. Verify if poetry is installed on your machine using `poetry --version`.
2. Clone this repository
3. In a terminal, navigate to the project's root folder
4. Use poetry to generate a new package called `math_api`. Refer to the documentation of the `poetry new` command to find out how to do that. This will generate the following project structure:
    ```
    .
    ├── math_api
    │   ├── README.md
    │   ├── math_api
    │   │   └── __init__.py
    │   ├── pyproject.toml
    │   └── tests
    │       └── __init__.py
    ```

## Exercise

1. Create a FastAPI app in `math_api/app.py` (so on the level of `pyproject.toml`) that serves your FastAPI API. The logic of your app should exist in `math_api/math_api/`. See FastAPI's ['first steps' documentation](https://fastapi.tiangolo.com/tutorial/first-steps/) to help you to get started. Manage your dependencies with poetry so that teammates could easily set up their own environments. Also try to make a distinction between dependencies for development and dependencies for code that runs in production.
2. Implement the following endpoints:
   - `/add` which accepts two parameters `a` and `b` and returns the result of `a+b`
   - `/sub` which accepts two parameters `a` and `b` and returns the result of `a-b`
   - `/mul` which accepts two parameters `a` and `b` and returns the result of `a*b`
   - `/div` which accepts two parameters `a` and `b` and returns the result of `a/b`
   - `/fib` which accepts a parameter `n` and returns [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_sequence) $F_n$
3. During development, pay attention to your [project structure](https://fastapi.tiangolo.com/tutorial/bigger-applications/) and add type hints for your methods and parameters.
5. Document your code with docstrings.
6. Write tests for each method with [`pytest`](https://pytest.org)
7. Format your code with black, isort and flake8.


**Extra:**
1. Install pre-commit and configure it so it runs black, flake8, isort and pytest.
2. Write a shell script that runs your tests and formatting checks, collects the return codes and writes a report to a file.
3. Package your app with poetry.
