import hashlib
import random

import requests


def send_sms_notification(phone: str | list, message: str) -> bool:
    LOGIN: str = "smartlife"
    PASSWORD: str = "sm@rtlife"
    MESSAGE: str = message

    if isinstance(phone, str):
        phone = [phone]
    phone = [str(p).replace("+", "") for p in phone]
    RECIPIENTS = ",".join(phone)
    APIKEY = hashlib.md5(f"{LOGIN}{PASSWORD}{MESSAGE}".encode("utf-8")).hexdigest()

    response = requests.get(
        "http://109.74.70.2:7678/sms_notification/sms.php",
        {
            "login": LOGIN,
            "apikey": APIKEY,
            "message": MESSAGE,
            "recipients": RECIPIENTS,
        },
    )

    result = int(response.text.split("<result>")[1].split("</result>")[0])
    return not bool(result)


def generate_otp() -> int:
    return random.randint(10000, 99999)
