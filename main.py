import os
import re
from dotenv import load_dotenv
from fastapi import FastAPI
from otp.melipayamak import Api

app = FastAPI()
load_dotenv()

api = Api(os.getenv("OTP_USERNAME"), os.getenv("OTP_PASSWORD"))
apiSoap = api.sms("soap")
apiRest = api.sms("rest")
_from = os.getenv("OTP_PHONE_NUMBER")


@app.get("/")
async def root():
    return {"message": "Welcome to Bimeh Sabz OTP Service! What are you locking for ?"}


@app.get("/getCredit")
async def get_credit():
    return apiSoap.get_credit()


@app.get("/getBasePrice")
async def get_base_price():
    return apiRest.get_base_price()


@app.post("/sendSMS")
async def send_sms(msg: str = "", number: str = ""):
    if msg == "":
        return {"status": "error", "msg": "empty sms body!"}
    else:
        if number == "":
            return {"status": "error", "msg": "empty phone number!"}
        else:
            if re.search("^09[0-9][0-9]{8}$", number):
                res_id = ""

                try:
                    res_id = apiSoap.send(number, _from, msg)
                    print(f"INFO:     SMS send with id {res_id} with soap")
                    return {"status": "success", "msg": "done!"}

                except ConnectionError:
                    print(f"INFO:     Error while sending SMS with soap service! - id: {res_id} - ConnectionError")

                    try:
                        res_id = apiRest.send(number, _from, msg)
                        print(f"INFO:     SMS send with id {res_id} with rest")
                        return {"status": "success", "msg": "done!"}

                    except ConnectionError:
                        print(f"INFO:     Error while sending SMS with rest service! - id: {res_id} - ConnectionError")
                        return {"status": "error", "msg": "message not delivered!"}
            else:
                return {"status": "error", "msg": "wrong phone number"}
