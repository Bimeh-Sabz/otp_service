FROM python:3.9

WORKDIR /otp

COPY ./ /otp

ARG OTP_PASSWORD
ARG OTP_USERNAME
ARG OTP_PHONE_NUMBER
ENV OTP_PASSWORD ${OTP_PASSWORD}
ENV OTP_USERNAME ${OTP_USERNAME}
ENV OTP_PHONE_NUMBER ${OTP_PHONE_NUMBER}

RUN pip install --no-cache-dir --upgrade -r /otp/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
