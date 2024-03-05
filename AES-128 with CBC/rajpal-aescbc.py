'''
------------------
Program details
------------------
Referred from: https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
Code uses AES-128 encryption (16 byte key) with CBC mode. Achieved through PyCryptoDome module.
-e option: Outputs IV, Ciphertext and key used to encrypt in JSON format
-d option: Expects the JSON string given after -e option. Outputs clear text.

The program gives an error if the respective options are not provided or if English is not provided

Test cases description:
1. Non English input
2. Help menu/Missing options
3. Encrypting a sentence
4. Decrypting a sentence
5. Incorrect key/ciphertext/iv provided


------------------
Test Cases
------------------

1. Case 1: Non English characters input. Here we input a spanish letter
──(root㉿kali)-[~/cryptography/programming3]
└─# python3 rajpal-aescbc.py -e "ABC24345á"
Error: Encryption data must be in English.

2. Case 2: No -e or -d provided
┌──(root㉿kali)-[~/cryptography/programming3]
└─# python3 rajpal-aescbc.py               
Usage:
rajpal-aescbc.py -e <data_to_encrypt> : Encrypt data
rajpal-aescbc.py -d '<json_string_to_decrypt>' : Decrypt data

Please provide a valid option and input.

3. Case 3: Encryption of a sentence
┌──(root㉿kali)-[~/cryptography/programming3]
└─# python3 rajpal-aescbc.py -e "Shhh. Here is the super secret password: 987654321" 
Encrypted: {"iv": "pKaDqhZcCrJVCvxfH8C6NA==", "ciphertext": "R+tEUmzsP9Pjclf2yuWRN7niKPofdHPHQNMZt95VJzht0sbMw2RmdOMHqo1j3KhyQGABrxETOwF/Dn/u13i9EA==", "key": "jeYtkx4nvC4j+ugXLZu3kw=="}

4. Case 4: Decryption of the same sentence
┌──(root㉿kali)-[~/cryptography/programming3]
└─# python3 rajpal-aescbc.py -d '{"iv": "pKaDqhZcCrJVCvxfH8C6NA==", "ciphertext": "R+tEUmzsP9Pjclf2yuWRN7niKPofdHPHQNMZt95VJzht0sbMw2RmdOMHqo1j3KhyQGABrxETOwF/Dn/u13i9EA==", "key": "jeYtkx4nvC4j+ugXLZu3kw=="}'
The message was: Shhh. Here is the super secret password: 987654321

5. Case 5: Wrong IV/Cipher/Key provided
Here, we change the key's first character "j" with "k"
┌──(root㉿kali)-[~/cryptography/programming3]
└─# python3 rajpal-aescbc.py -d '{"iv": "pKaDqhZcCrJVCvxfH8C6NA==", "ciphertext": "R+tEUmzsP9Pjclf2yuWRN7niKPofdHPHQNMZt95VJzht0sbMw2RmdOMHqo1j3KhyQGABrxETOwF/Dn/u13i9EA==", "key": "keYtkx4nvC4j+ugXLZu3kw=="}'
Incorrect decryption




'''

import sys
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def is_english(text):
    try:
        # Check if the text is ASCII encodable which might be a good enough approximation for English
        text.encode('ascii')
    except UnicodeEncodeError:
        return False
    return True

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct, 'key': b64encode(key).decode('utf-8')}

def decrypt(encrypted_data):
    try:
        b64 = json.loads(encrypted_data)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        key = b64decode(b64['key'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return "The message was: " + pt.decode('utf-8')
    except (ValueError, KeyError) as e:
        return "Incorrect decryption"

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['-e', '-d']:
        print("Usage:")
        print(f"{sys.argv[0]} -e <data_to_encrypt> : Encrypt data")
        print(f"{sys.argv[0]} -d '<json_string_to_decrypt>' : Decrypt data")
        print("\nPlease provide a valid option and input.")
    else:
        option, data = sys.argv[1], sys.argv[2]
        if option == '-e':
            if not is_english(data):
                print("Error: Encryption data must be in English.")
                return
            key = get_random_bytes(16)
            encrypted_data = encrypt(data, key)
            print("Encrypted:", json.dumps(encrypted_data))
        elif option == '-d':
            decryption_result = decrypt(data)
            print(decryption_result)

if __name__ == "__main__":
    main()
