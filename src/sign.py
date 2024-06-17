import uuid
import time
import base64
import hmac
import hashlib


def sign_token(token, secret):
    # https://github.com/OpenWonderLabs/SwitchBotAPI
    # -> How to Sign?

    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

    # t, sign, nonce
    return (str(t), str(sign, 'utf-8'), str(nonce))
