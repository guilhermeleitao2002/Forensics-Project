#!/usr/bin/python
import base64
from Crypto.Cipher import AES
import hashlib

password = "CZN.pjp0paz3jej5jgajcj!hzx3yzp2DTB1hgy"

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return cipher.decrypt(enc[16:])

with open("decrypted", "wb") as f:
    with open("encrypted", "rb") as e:
        data = e.read()
        f.write(decrypt(data, password))