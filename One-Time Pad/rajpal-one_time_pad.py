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
