# module used to generate prime numbers: PyCryptodome
# pip install pycryptodome==3.14.1

from Crypto.Util.number import getPrime
import hashlib
import random
import math

# ************** PART a ******************

def generate_prime_numbers(bits):
    """
    Generate a prime numbers of a given number of bits.
    """
    p = getPrime(bits)
    q = getPrime(bits)
    return p, q

# ************** PART b ******************

def robin_miller_test(n,k=10):
    """
    Test if a number is composite or probably prime.
    params:
        n: the number to test
        k: the number of testing rounds
    """
    # 2 is only even prime
    if n == 2:
        return True
    # None of even numbers other than 2 are prime
    if n % 2 == 0:
        return False
    # write n as 2^s*d where d is odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    # do k tests
    
    for i in range(k):
        # a is witness for compositeness if a^d mod n != 1
        # and a^(2^i*d) mod n != n-1 for some a
        a = random.randint(2, n - 2)
        # x = a^d mod n
        x = pow(a, d, n)

        # if x = 1 or x = n-1 then continue to next iteration
        if x != 1 and x != n - 1:
            # check whether any other x is a factor of n    
            for j in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                elif x == n - 1:
                    break
            # if we got here, then n is not a prime
            return False
    # if we got here, n is prime

    return True

    
# ************** PART c ******************

def euclid_gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

# ************** PART d ******************

def extended_euclid_iterative(a, b):
    """
    Calculate the greatest common divisor of two numbers and the coefficients of the Bezout identity such that a*s + b*t = gcd(a,b).
    """
    # initialize the coefficients of the Bezout identity
    old_s, s = 1, 0
    old_t, t = 0, 1
    # calculate the coefficients of the Bezout identity
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return (a, old_s, old_t)

# ************** PART e ******************
# SHA256 hash function
def hash_function(message):
    """
    Hash a message using SHA256.
    """
    hash = hashlib.sha256()
    hash.update(message.encode('utf-8'))
    return hash.hexdigest()



# ************** PART f ******************



# helper class for RSA
class RSA:
    """
    Encrypt and decrypt messages using RSA.
    """

    def __init__(self, bits):
        """
        Generate a public and private key.
        """
        self.bits = bits
        self.p, self.q = generate_prime_numbers(bits)
        # check if p and q are prime
        while not robin_miller_test(self.p) or not robin_miller_test(self.p):
            self.p, self.q = generate_prime_numbers(bits)


        self.N = self.p * self.q
        # use euclid_gcd to find e such that e and (p-1)(q-1) are coprime
        # pick random number as e
        e_=random.randint(2, self.N - 2)
        while euclid_gcd(e_, (self.p - 1) * (self.q - 1)) != 1:
            e_=random.randint(2, self.N - 2)
        self.e = e_
        # Public key is (e, N)

        # use extended_euclid_iterative to find d such that d*e mod (p-1)(q-1) = 1
        self.d = extended_euclid_iterative(self.e, (self.p-1)*(self.q-1))[1]
        # Private key is (d, N)
        # public key of other party to be set later
        self.other_e = None
        self.other_N = None
        

    def get_public_key(self):
        """
        Return the public key.
        """
        return self.e, self.N

    def set_other_public_key(self, e, N):
        """
        Set the public key of the other party.
        """
        self.other_e = e
        self.other_N = N
    
    def encrypt(self, message):
        """
        Encrypt a message using RSA.
        """
        return pow(self.string_to_int(message), self.other_e, self.other_N)
    def decrypt(self, message):
        """
        Decrypt a message using RSA.
        """
        return self.int_to_string(pow(message, self.d, self.N))

  
    #signing and verifying
    def sign(self, message):
        """
        Sign a message using RSA.
        """
        return pow(self.string_to_int(hash_function(message)), self.d, self.N)
    def verify(self, signature, message):
        """
        Verify a signature using RSA.
        """
        return hash_function(message) == self.int_to_string(pow(signature, self.other_e, self.other_N))
    def string_to_int(self,message):
        """
         Convert a string to an integer.
         """
        return int.from_bytes(message.encode('utf-8'), 'big')

    def int_to_string(self,message):
        """
         Convert an integer to a string.
         """
        return message.to_bytes(math.ceil(message.bit_length() / 8) , 'big').decode('utf-8')




# Alice generate a key pair
bits = 1024
alice = RSA(bits)
bob = RSA(bits)
# alice public key
# Alice and Bob share the public key
alice_e, alice_N = alice.get_public_key()
bob_e, bob_N = bob.get_public_key()
# exchanging keys
alice.set_other_public_key(bob_e, bob_N)
bob.set_other_public_key(alice_e, alice_N)
# Now Alice and Bob can exchange messages

# Alice is sending message to Bob
message = "Hello Bob"
# Alice encrypts the message using Bob's public key
alice_message = alice.encrypt(message)
print("Alice encrypts the following message:", message)
print("Alice send encrypted message to Bob with the signature:")
# Alice signs the message using her private key
signature = alice.sign(message)
# Bob decrypts the message using Bob's private key
message_decrypted = bob.decrypt(alice_message)
# Bob verifies the signature using Alice's public key
if bob.verify(signature, message_decrypted):
    print("Bob verified the signature")
else:
    print("Bob failed to verify the signature")
print("Bob decrypts the message:", message_decrypted)

# # Bob is sending message to Alice
# message = "Hello Alice"
# # Bob encrypts the message using Alice's public key
# bob_message = bob.encrypt(message)
# print("Bob encrypts the following message:", message)
# print("Bob send encrypted message to Alice with the signature:")
# # Bob signs the message using his private key
# signature = bob.sign(message)
# # Alice decrypts the message using Alice's private key
# message_decrypted = alice.decrypt(bob_message)
# # Alice verifies the signature using Bob's public key
# if alice.verify(signature, message_decrypted):
#     print("Alice verified the signature")
# else:
#     print("Alice failed to verify the signature")
# print("Alice decrypts the message:", message_decrypted)