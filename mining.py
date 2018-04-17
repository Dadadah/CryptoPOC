import hashlib
import bcrypt
import base64
import cryptoutil as cu

testmessage = "Hello World"

nonce = 0
count = 0
totalnonce = 0

difficulty = 2**5

done = False
testing = True

salt = bcrypt.gensalt(12)

while(not done):
    totalmessage = str(testmessage) + str(nonce)
    totalmessage = totalmessage.encode('utf-8')
    hashed = bcrypt.hashpw((cu.hash_hex_val(totalmessage)).encode('utf-8'), salt)
    vals = hashed.split(b'$')
    val = base64.b64decode(vals[3][22:] + b'=', './')
    val = cu.get_int(val)
    nonce = nonce + 1
    if val % difficulty == 0:
        print('Hash Found!')
        totalnonce = totalnonce + nonce
        nonce = 0
        count = count + 1
        if count > 10:
            done = True

print(totalnonce/count)
