if __name__ == "__main__":
    
    private_key, public_key = generateKey(nbits = 1028) # Generate private and public key n-bits long.

    data_1 = 29 # Example of data. 
    data_2 = 31  # Example of data. 

    encrypt_data_1 = encrypt(data_1, public_key) # Encrypt data.
    encrypt_data_2 = encrypt(data_2, public_key) # Encrypt data.

    sum_encrypted_data = addEncrypted(encrypt_data_1, encrypt_data_2, public_key) # Add elements .

    score  = decrypt(sum_encrypted_data, private_key) # Decrypt data.

    print(score) 
    >>> 60
