from gmpy2 import random_state, mpz_random, powmod, mul, div

"""  Brief explanation of imported functions:
        random_state: returns a new object containing state information for the random number generator.
        mpz_random: returns a uniformly distributed random integer between 0 and n-1.
        powmod: returns (x**y) mod m.
        mul: returns the multiplication of x and y.
        div: returns the division of x and y.

    gmpy2 documentation: https://readthedocs.org/projects/gmpy2/downloads/pdf/latest/
"""

def encrypt(data, public_key):

    """ This function encrypts your data """

    g, n = public_key # Get public KEY
    n2 = mul(n,n)  # n**2 used in next calculations.

    seed = random_state(hash(random_state())) # Seed used to generate random number.
    r = mpz_random(seed, n - 1 ) + 1 # Select random INTEGER g from Z. Where Z is set of values ​​from 1 to n**2.
    
    if type(data) == int : data = [data] # Change type to list if not.
    
    const_num = powmod(r, n, n2) # Const used to next calculation.
    encrypted_numbers = [ mul(powmod(g, value, n2), const_num) % n2 for value in data ] # Compute ciphertext E(m) = g**m * r**n mod n**2 where m is number

    return encrypted_numbers

def decrypt(encrypted_data, private_key):

    """ This function decrypts your data """

    def eucDiv(val,n): # The quotient of the Euclidean division. 
        return div(val - 1, n) 

    alpha, mu, n = private_key # Get private KEY

    return mul(eucDiv(powmod(encrypted_data , alpha, mul(n, n)), n), mu) % n # m = eucDiv(m**alpha mod n**2, n) * mu mod n where m is your decrypted number.
