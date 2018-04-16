import sys
import random
import primes
import hashlib

class BlumBlumShub(object):


    def getPrime(self, bits=256):
        """
        Generate appropriate prime number for use in Blum-Blum-Shub.

        This generates the appropriate primes (p = 3 mod 4) needed to compute the
        "n-value" for Blum-Blum-Shub.

        bits - Number of bits in prime

        """
        while True:
            p = primes.bigppr(bits)
            if p & 3 == 3:
                return p

    def generateN(self, bits=512):
        """
        This generates the "n value" for use in the Blum-Blum-Shub algorithm.

        bits - The number of bits of security
        """

        p = self.getPrime(int(bits/2))
        while 1:
            q = self.getPrime(int(bits/2))
            # make sure p != q (almost always true, but just in case, check)
            if p != q:
                return p * q

    def __init__(self, bits, initialseed):
        """
        Constructor, specifing bits for n.

        bits - number of bits
        """
        self.n = self.generateN(bits)
        # print "n set to " + repr(self.n)
        length = self.bitLen(self.n)
        self.setSeed(initialseed)

    def setSeed(self, seed):
        """
        Sets or resets the seed value and internal state.

        seed -The new seed
        """

        self.state = seed % self.n

    def bitLen(self, x):
        " Get the bit lengh of a positive number"
        assert x > 0
        q = 0
        while x:
            q += 1
            x >>= 1
        return q

    def next(self, numBits):
        "Returns up to numBit random bits"

        result = 0
        for i in range(numBits):
            self.state = (self.state**2) % self.n
            result = (result << 1) | (self.state&1)

        return result

if __name__ == "__main__":

    hash = hashlib.sha256()
    hash.update(b"Interior Crocodile Alligator")
    bbs = BlumBlumShub(128, int.from_bytes(hash.digest(), byteorder="big"));

    #print "Generating 10 numbers"

    for i in range (256):
        print(bbs.next(256))
