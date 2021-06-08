from secrets import randbits
from gmpy2 import next_prime, is_prime

"""  Brief explanation of imported functions:
        randbits: genarete n-bit number.
        next_prime: returns the next probable prime number.
        is_prime: return True if number is probably prime. 
        
    secrets documentation: https://docs.python.org/3/library/secrets.html
    gmpy2 documentation: https://readthedocs.org/projects/gmpy2/downloads/pdf/latest/
"""
def generatePrimeNumbers(nbits):

    """ This function generate two n-bits Safe prime numbers.
        Where:
            nbits: The number of bits in generete number. """

    def generatePrime(nbits):

        """ This function generate n-bits Prime number. """

        number = randbits(nbits) # Genarete n-bits number.
        odd_number = (number&(number - 1)) + 1 # Change number to odd number.
        prime_number = next_prime(odd_number) # Finding a prime number starting with an odd_number.

        return prime_number

    def generateSafePrime(nbits):
        
        """ This function generate n-bits Safe prime number. """ 

        while True:
            prime_number = generatePrime(nbits - 1) # Generate (n-bits - 1) Prime number.
            safe_prime_number = 2 * prime_number - 1  # Calculation of n-bits Safe prime number.
            if (is_prime(safe_prime_number)): # Checking if the calculated Number is prime.
                return safe_prime_number

    fisrt_number = generateSafePrime(nbits) # Generation of the first prime number.
    second_number = generateSafePrime(nbits) # Generation of the second prime number.
    while fisrt_number == second_number :  # Fisrt and second prime number can't be the same.
        second_number = generateSafePrime(nbits)
    
    return fisrt_number, second_number
