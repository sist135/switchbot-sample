import os
import requests
from dotenv import load_dotenv

from sign import sign_token

# .envファイルからトークンを読み込む
load_dotenv()
SWITCHBOT_TOKEN = os.getenv('SWITCHBOT_TOKEN')
SWITCHBOT_SECRET = os.getenv('SWITCHBOT_SECRET')
DEVICE_ID = os.getenv('DEVICE_ID')


def turn_off():
    t, sign, nonce = sign_token(SWITCHBOT_TOKEN, SWITCHBOT_SECRET)
    url = f'https://api.switch-bot.com/v1.1/devices/{DEVICE_ID}/commands'
    headers = {
        "Authorization": SWITCHBOT_TOKEN,
        "Content-Type": "application/json",
        "charset": "utf8",
        "t": t,
        "sign": sign,
        "nonce": nonce,
    }
    payload = {
        "command": "turnOff",
        "parameter": "default",
        "commandType": "command"
    }
    res = requests.post(url, headers=headers, json=payload)
    if res.status_code == 200:
        print("success")
    else:
        print("failure", res.status_code, res.text)


def main():
    turn_off()


if __name__ == '__main__':
    main()
