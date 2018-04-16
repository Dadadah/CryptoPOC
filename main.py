import hashlib
import secrets

def hash_val(bytestring):
    hash = hashlib.sha256()
    hash.update(bytestring)
    return hash.digest()

def get_int(bytestring):
    return int.from_bytes(bytestring, byteorder="big")


def generate_private_key(x):
    newprivkey = []
    for x in range(x):
        newprivkey.append(secrets.randbits(256))
    return newprivkey


def generate_public_key(privkey):
    newpubkey = []
    for x in range(len(privkey)):
        newpubkey.append(get_int(hash_val(privkey[x].to_bytes(32, byteorder="big"))))
    return newpubkey


privatekey = generate_private_key(512)
publickey = generate_public_key(privatekey)

print('BEGIN PRIVATE KEY')
print(privatekey)
print('END PRIVATE KEY')
print('BEGIN PUBLIC KEY')
print(publickey)
print('END PUBLIC KEY')


while True:
    val = input()
    newdigest = hash_val(val.encode('utf-8'))
    print('Message: ' + val)
    print('Digest: ' + str(newdigest))
    intrep = get_int(newdigest)
    sig = []
    for x in range(256):
        select = 1 if (intrep & (1 << x)) else 0
        sig.append(privatekey[x*2 + select])
    print('BEGIN SIGNATURE')
    print(sig)
    print('END SIGNATURE')
    verification = []
    for x in range(256):
        select = 1 if (intrep & (1 << x)) else 0
        verification.append(publickey[x*2 + select])
    test = []
    for x in range(256):
        test.append(get_int(hash_val(sig[x].to_bytes(32, byteorder="big"))))
    print('Transaction verified?: ' + str(verification == test))
