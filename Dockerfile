FROM python:3.9

WORKDIR /otp

COPY ./ /otp

RUN pip install --no-cache-dir --upgrade -r /otp/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
