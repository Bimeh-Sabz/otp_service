import os

from fastapi import FastAPI

app = FastAPI()
#name = os.getenv("MY_NAME")


@app.get("/")
async def root():
    return {"message": "Welcome to Bimeh Sabz OTP Service! What are you locking for ?"}


@app.get("/getBasePrice")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
