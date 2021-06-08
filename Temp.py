from gmpy2 import powmod, mul, div
from secrets import randbelow

def encrypt(data, public_key):

    """ This function encrypts your data """

    g, n = public_key # Get public KEY
    n2 = mul(n,n)  # n**2 used in next calculations.

    r = randbelow(n-1) + 1 # Select random INTEGER g from Z. Where Z is set of values ​​from 1 to n**2.
    
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
