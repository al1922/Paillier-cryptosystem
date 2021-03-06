from key import generateKey
from crypt import encrypt, decrypt
from cryptAdd import addEncrypted, addAllEncrypted

if __name__ == "__main__":
    
    private_key, public_key = generateKey(nbits = 128) # Generate private and public key n-bits long.

    data = [20, 50, 70, 120] # Example of data. 

    encrypt_data = encrypt(data, public_key) # Encrypt data.

    sum_encrypted_data = addAllEncrypted(encrypt_data, public_key) # Add all .

    score  = decrypt(sum_encrypted_data, private_key) # Decrypt data.

    print(score)
