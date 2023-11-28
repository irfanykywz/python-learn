import pyotp

key = 'keyotp'

# build
otp = pyotp.TOTP(f'base32{key}')
generate = otp.now()
print(generate)

# validate
print(otp.verify(generate))
# return bool


# facebook otp 
totp = pyotp.TOTP("7HTGZ5VOSSNPM2YORAXIQJYLGX5J43CF")
print("Current OTP:", totp.now())