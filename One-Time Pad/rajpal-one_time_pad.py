"""

Name:  Harshit Rajpal

NetID: hr2404



The code implements a rudimentary One Time Pad

The code takes in plain English text message as input, then XORs it with a Hexadecimal key to create an encrypted text which is also hexadedcimal



To use this code, a help menu is given as well. Please find below two test cases where a single word and multiple words are encrypted then decrypted using the right key

Then in the final test case, wrong key is  given to decrypt a text.



____________________________________________________________________________________________

Case 1: Single word encryption

┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py                                                          

Error: Please specify either -e for encryption or -d for decryption.



┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py -e HELLOHELLO

Encrypted Text: 240be99e0616bb31d3a5

Key: 6c4ea5d2495efe7d9fea

                                                                                                    

┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py -d --text 240be99e0616bb31d3a5 --key 6c4ea5d2495efe7d9fea

Decrypted Text: HELLOHELLO



____________________________________________________________________________________________



Case 2: Sentence encryption and decryption



For a sentence, message is to be encrypted in quotation marks



┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py -e "Hello TAs, this is Harshit."                         

Encrypted Text: 7b31a8ae0b78944d176029d79fee655ed9430da2dae74f8d2b2d00

Key: 3354c4c26458c00c644c09a3f787167eb0302deabb953ce542592e

                                                                                                    

┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py -d --text 7b31a8ae0b78944d176029d79fee655ed9430da2dae74f8d2b2d00 --key 3354c4c26458c00c644c09a3f787167eb0302deabb953ce542592e

Decrypted Text: Hello TAs, this is Harshit.



____________________________________________________________________________________________



Case 3: Wrong key used

The program gives an error in this case. See how I have changed the correct key.



┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py -e HELLOHELLO                                            

Encrypted Text: 2e399e1e0470095c28bb

Key: 667cd2524b384c1064f4



┌──(root㉿kali)-[~/cryptography/programming2]

└─# python3 rajpal-one_time_pad.py -d --text 240be99e0616bb31d3a5 --key 557ab2524b989f5678c4

Traceback (most recent call last):

  File "/root/cryptography/programming2/rajpal-one_time_pad.py", line 67, in <module>

    main()

  File "/root/cryptography/programming2/rajpal-one_time_pad.py", line 60, in main

    print(f"Decrypted Text: {decrypted.decode('utf-8')}")

                             ^^^^^^^^^^^^^^^^^^^^^^^^^

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcc in position 3: invalid continuation byte





"""





import os

import binascii

import argparse



def generate_key(length):

    return os.urandom(length)



def xor_encrypt(text, key):

    return bytes([a ^ b for a, b in zip(text, key)])



def xor_decrypt(encrypted, key):

    return bytes([a ^ b for a, b in zip(encrypted, key)])



def to_hex(data):

    return binascii.hexlify(data).decode('utf-8')



def from_hex(data):

    return binascii.unhexlify(data)



def parse_arguments():

    parser = argparse.ArgumentParser(description='Encrypt or Decrypt text using XOR and a generated key.')

    parser.add_argument('-e', '--encrypt', help='Encrypt the specified text.', metavar='TEXT', type=str)

    parser.add_argument('-d', '--decrypt', help='Decrypt the specified text with a key.', action='store_true')

    parser.add_argument('--text', help='Input text for encryption or decryption.', metavar='TEXT', type=str, required=False)

    parser.add_argument('--key', help='Key for decryption in hexadecimal.', metavar='KEY', type=str, required=False)

    return parser.parse_args()



def main():

    args = parse_arguments()

    

    if args.encrypt:

        text_bytes = args.encrypt.encode('utf-8')

        key = generate_key(len(text_bytes))

        encrypted = xor_encrypt(text_bytes, key)

        print(f"Encrypted Text: {to_hex(encrypted)}")

        print(f"Key: {to_hex(key)}")

    elif args.decrypt:

        if args.text and args.key:

            encrypted_bytes = from_hex(args.text)

            key_bytes = from_hex(args.key)

            decrypted = xor_decrypt(encrypted_bytes, key_bytes)

            print(f"Decrypted Text: {decrypted.decode('utf-8')}")

        else:

            print("Error: Both encrypted text and key are required for decryption.")

    else:

        print("Error: Please specify either -e for encryption or -d for decryption.")



if __name__ == "__main__":

    main()

