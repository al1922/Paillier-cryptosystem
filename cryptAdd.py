from gmpy2 import mul, div
from functools import reduce

"""  Brief explanation of imported functions:
        mul: returns the multiplication of x and y.
        div: returns the division of x and y.
        reduce: apply the specified function passed in its argument to all list items.

    gmpy2 documentation: https://readthedocs.org/projects/gmpy2/downloads/pdf/latest/
"""

def addEncrypted(first_encrypted_number, second_encrypted_number, public_key):

    """ This function add your numbers"""

    _, n = public_key # Get public KEY.

    return mul(first_encrypted_number, second_encrypted_number) % mul(n,n) # Add two encrypted numbers. E(m1)*E(m2) mod n**2 


def addAllEncrypted(encrypted_data, public_key):

    """ This function add all elements in list """

    _, n = public_key # Get public KEY.
    n2 = mul(n,n) # n**2 used in next calculations.
    
    sorce = encrypted_data[0]
    for itr in range(1, len(encrypted_data)): 
        sorce = mul(sorce, encrypted_data[itr]) % n2  # Add encrypted numbers. E(m1)*E(m2) mod n**2 

    return sorce