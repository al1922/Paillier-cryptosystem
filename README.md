# Paillier cryptosystem

## General info
This project is an implementation of a Paillier cryptosystem.<br />
If you have any questions, please feel free to write to me.<br />

## Technologies
Project is created with:
* Python version: 3.9.0
* gmpy2 version: 2.0.8

## Setup 
Lots of people have trouble properly installing <code>gmpy2</code> module.<br />
You can do it as follows:

1. Go to <code>https://www.lfd.uci.edu/~gohlke/pythonlibs/</code> and find the column **GMPY**.
2. Make sure that your **python vesrion** is the same like **gmpy2**.<br /> For example, I have **python version 3.9**, so i need download **gmpy2‑2.0.8‑cp39‑cp39‑win_amd64.whl**.<br /> <code>cp39 = python version 3.9.0 </code>
3. Go to your terminal and run: ```pip install C:\Users\Downloads\gmpy2-2.0.8-cp39-cp39-win_amd64.whl``` <br/> Make sure that the file name is the same as name on the page where you downloaded it.
4. Go to your terminal and run: ```pip show gmpy2``` and find **Location**.<br/> For example,on my computer is: c:\users\itakciezjem\appdata\local\programs\python\python39\lib\site-packages
5. Find file with name <code>gmpy2.cp39-win_amd64.pyd</code> copy and paste into ***lib*** folder.<br/> On my computer is: c:\users\itakciezjem\appdata\local\programs\python\python39\lib

## Use 

```
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
    >> 260
```
