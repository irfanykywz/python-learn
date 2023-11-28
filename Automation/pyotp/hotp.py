import pyotp

key = 'keyotp'

otp = pyotp.HOTP(f'base32{key}')

# generate
h1 = otp.at(0)
h2 = otp.at(1)
h3 = otp.at(2)
h4 = otp.at(333)

# validate [secret,index]
print(otp.verify(h1, 0))
print(otp.verify(h2, 1))
print(otp.verify(h3, 2))
print(otp.verify(h4, 333))

# return True