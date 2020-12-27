from gmpy2 import gcd, lcm, random_state, mpz_random, invert, powmod, mul, div
from prime import generatePrimeNumbers

"""  Brief explanation of imported functions:
        gcd: returns the greatest common divisor of integers a and b.
        lcm: returns the lowest common multiple of integers a and b.
        random_state: returns a new object containing state information for the random number generator.
        mpz_random: returns a uniformly distributed random integer between 0 and n-1.
        invert: returns y such that x*y== 1 modulo m, or 0 if no such y exists.
        powmod: returns (x**y) mod m.
        mul: returns the multiplication of x and y.
        div: returns the division of x and y.
        safePrimeNumbers: returns two safe prime numbers.

    gmpy2 documentation: https://readthedocs.org/projects/gmpy2/downloads/pdf/latest/
"""

def generateKey(nbits):

    def eucDiv(val,n): # The quotient of the Euclidean division. 
        return div(val - 1, n) 

    while True:

        """ Key generation scheme """

        fisrt_prime, second_prime = generatePrimeNumbers(nbits) # Generate two prime Numbers of equivalent bit length p and q. 

        while gcd(mul(fisrt_prime, second_prime), mul((fisrt_prime - 1), (second_prime - 1))) != 1:  # Confirm that gcd(p*q, (p − 1)*(q − 1)) = 1.
            fisrt_prime, second_prime = generatePrimeNumbers(nbits) # If not, generate NEW prime numbers.

        n = mul(fisrt_prime, second_prime) # Calculate n = p*q.
        n2 = mul(n,n) # n**2 used in next calculations.

        alpha = lcm(fisrt_prime - 1, second_prime - 1) # Calculate alpha =  lcm(p - 1, q - 1).

        seed = random_state(hash(random_state())) # Seed used to generate random number.
        g = mpz_random(seed, n2 - 1 ) + 1  # Select random INTEGER g from Z. Where Z is set of values ​​from 1 to n**2.

        try:

            mu = invert(eucDiv(powmod(g, alpha, n2), n), n) # Calculate the modular multiplicative inverse. mu = (eucDiv( g**alpha mod n**2 ))**-1 mod n
            
            private_key = [alpha, mu, n] # Private KEY.
            public_key = [g, n]       # Public KEY.
            
            return private_key, public_key

        except Exception:
            pass