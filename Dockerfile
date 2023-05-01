FROM python:3.10

RUN mkdir /app
RUN pip install poetry

COPY ./math_api /app

WORKDIR /app

RUN poetry config virtualenvs.create false
RUN poetry install

ENTRYPOINT ["uvicorn", "math_api.app:app", "--host", "0.0.0.0", "--port", "80"]
