import hashlib
import secrets
from blum import BlumBlumShub
import cryptoutil as cu
from merkletree import MerkleNode

bitlevel = 8
security = 256


def generate_private_key(x):
    global bbs
    newprivkey = []
    for x in range(x):
        newprivkey.append(bbs.next())
    return newprivkey


def generate_public_key(privkey):
    newpubkey = []
    for x in range(len(privkey)):
        newpubkey.append(cu.get_int(cu.hash_val(cu.get_bytes(privkey[x]))))
    return newpubkey

bbs = BlumBlumShub(security, b"I drive a chevrolet movie theater", cu.get_int(cu.hash_val(b"Interior Crocodile Alligator")))
merkle = MerkleNode(bitlevel)

for x in range(2**bitlevel):
    privatekey = generate_private_key(security*2)
    publickey = generate_public_key(privatekey)
    hash = hashlib.sha256()
    for key in publickey:
        hash.update(cu.get_bytes(key))
    temp = merkle.get_child(x)
    temp.hash = hash.hexdigest()

merkle.update_tree()

print(merkle.hash)

'''
while True:
    val = input()
    newdigest = cu.hash_val(val.encode('utf-8'))
    print('Message: ' + val)
    print('Digest: ' + str(newdigest))
    intrep = cu.get_int(newdigest)
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
        test.append(cu.get_int(cu.hash_val(cu.get_bytes(sig[x]))))
    print('Transaction verified?: ' + str(verification == test))
'''
