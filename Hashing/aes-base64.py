# https://stackoverflow.com/questions/12524994/encrypt-and-decrypt-using-pycrypto-aes-256
from base64 import b64decode, b64encode
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):
    
    def __init__(self = None, key = None):
        self.key = sha256(key.encode()).digest()

    
    def encrypt(self = None, raw = None):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw.encode()))

    
    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    
    def _pad(self, s):
        bs = AES.block_size
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    _unpad = staticmethod(_unpad)



ae = AESCipher('secretKiy')

enc = ae.encrypt('hello world')
print(enc)

dec = ae.decrypt(enc)
print(dec)