import hashlib
import bcrypt

testmessage = "Hello World"

nonce = 0
count = 0
totalnonce = 0

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
    val = list(vals[3][22:])
    nonce = nonce + 1
    if val[0] == 100:
        testmessage = vals[3][22:]
        totalnonce = totalnonce + nonce
        nonce = 0
        count = count + 1
        if count > 10:
            done = True

print(totalnonce/count)
