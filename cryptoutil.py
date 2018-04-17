import hashlib

def hash_val(bytestring):
    hash = hashlib.sha256()
    hash.update(bytestring)
    return hash.digest()


def hash_hex_val(bytestring):
    hash = hashlib.sha256()
    hash.update(bytestring)
    return hash.hexdigest()


def get_int(bytestring):
    return int.from_bytes(bytestring, byteorder="big")


def get_bytes(num, size=32):
    return num.to_bytes(size, byteorder="big")
