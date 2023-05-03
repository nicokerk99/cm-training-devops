FROM python:3.10
LABEL org.opencontainers.image.source="https://github.com/nicokerk99/cm-training"

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["uvicorn", "math_api.app:app", "--host", "0.0.0.0", "--port", "80"]
