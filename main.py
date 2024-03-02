import pyotp ## Base32 , https://cryptii.com/pipes/base32
secret_key = 'JJXWQ3STNZXXOMBXKNSXA5DFNVRGK4RRHA2TIQTSN5QWIU3UOJSWK5A=' ## JohnSnow07September1854BroadStreet
totp = pyotp.TOTP(secret_key) ; otp = totp.now()
print('pyotp:',otp)
