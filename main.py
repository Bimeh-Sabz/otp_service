import os
from fastapi import FastAPI
from otp.melipayamak import Api

app = FastAPI()
api = Api(os.getenv("OTP_USERNAME"), os.getenv("OTP_PASSWORD")).sms("soap")


@app.get("/")
async def root():
    return {"message": "Welcome to Bimeh Sabz OTP Service! What are you locking for ?"}


@app.get("/getBasePrice")
async def get_base_price():
    return {"price": api.get_credit()}
