import os

from dotenv import load_dotenv
from fastapi import FastAPI
from otp.melipayamak import Api

app = FastAPI()
load_dotenv()
apiSoap = Api(os.getenv("OTP_USERNAME"), os.getenv("OTP_PASSWORD")).sms("soap")
apiRest = Api(os.getenv("OTP_USERNAME"), os.getenv("OTP_PASSWORD")).sms("rest")
_from = os.getenv("OTP_PHONE_NUMBER")


@app.get("/")
async def root():
    return {"message": "Welcome to Bimeh Sabz OTP Service! What are you locking for ?"}


@app.get("/getCredit")
async def get_credit():
    return apiSoap.get_credit()


@app.get("/getBasePrice")
async def get_base_price():
    return {"price": api.get_credit()}
