import os
import requests
import json
from dotenv import load_dotenv

from sign import sign_token

# .envファイルからトークンを読み込む
load_dotenv()
SWITCHBOT_TOKEN = os.getenv('SWITCHBOT_TOKEN')
SWITCHBOT_SECRET = os.getenv('SWITCHBOT_SECRET')

# デバイス一覧を取得する


def get_all_devices():
    t, sign, nonce = sign_token(SWITCHBOT_TOKEN, SWITCHBOT_SECRET)
    url = "https://api.switch-bot.com/v1.1/devices"
    headers = {
        'Authorization': SWITCHBOT_TOKEN,
        'Content-Type': 'application/json',
        'charset': 'utf8',
        't': t,
        'sign': sign,
        'nonce': nonce,
    }
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        return response.json()
    else:
        raise "Failed to fecth data."


def main():
    res = get_all_devices()
    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
