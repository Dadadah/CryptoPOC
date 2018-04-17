import sys
import random
import hashlib
import gmpy2
import cryptoutil as cu

class BlumBlumShub(object):
    def getPrime(self, bits):
        while True:
            prime = random.getrandbits(bits) | 1
            if gmpy2.is_strong_bpsw_prp(prime):
                if prime & 3 == 3:
                    return prime


    def generateVals(self, bits):
        self.p = self.getPrime(int(bits/2))
        while True:
            self.q = self.getPrime(int(bits/2))
            # make sure p != q (almost always true, but just in case, check)
            if self.p != self.q:
                self.m = self.p * self.q
                return


    def __init__(self, bits, primeseed, initialseed):
        random.seed(primeseed)
        self.generateVals(bits)
        self.setSeed(initialseed)


    def setSeed(self, seed):
        while seed < 3 or seed%self.p == 0 or seed%self.q == 0:
            seed = cu.get_int(cu.hash_val(cu.get_bytes(seed)))
        self.state = seed


    def next(self):
        self.state = (self.state**2) % self.m
        return self.state


if __name__ == "__main__":
    bbs = BlumBlumShub(256, b"I drive a chevrolet movie theater", cu.get_int(cu.hash_val(b"Interior Crocodile Alligator")));

    for i in range (256):
        print(bbs.next())
