import os
import requests
from dotenv import load_dotenv


load_dotenv()

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")


if not ZAPI_INSTANCE_ID or not ZAPI_TOKEN:
    raise ValueError(
        "As variáveis ZAPI_INSTANCE_ID e ZAPI_TOKEN não foram definidas.")

BASE_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}"


def send_message(number: str, contact_name: str) -> bool:

    url = f"{BASE_URL}/send-text"
    payload = {
        "phone": number,
        "message": f"Olá {contact_name}, tudo bem com você?"
    }
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN,

    }
    try:
        response = requests.post(
            url, json=payload, headers=headers, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False
