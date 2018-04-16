import hashlib
import bcrypt
import base64

testmessage = "Hello World"

nonce = 0
count = 0
totalnonce = 0

difficulty = 4

done = False
testing = True

salt = bcrypt.gensalt(12)

while(not done):
    hash = hashlib.sha256()
    totalmessage = str(testmessage) + str(nonce)
    totalmessage = totalmessage.encode('utf-8')
    hash.update(totalmessage)
    hashed = bcrypt.hashpw((hash.hexdigest()).encode('utf-8'), salt)
    vals = hashed.split(b'$')
    val = base64.b64decode(vals[3][22:] + b'=', './')
    val = int.from_bytes(val, byteorder='big')
    nonce = nonce + 1
    if val % difficulty == 0:
        print('Hash Found!')
        totalnonce = totalnonce + nonce
        nonce = 0
        count = count + 1
        if count > 10:
            done = True

print(totalnonce/count)
