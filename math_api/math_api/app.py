from fastapi import FastAPI

from math_api.api.router import router

app = FastAPI(title="Calculator API")
app.include_router(router)
