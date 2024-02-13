def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            isUpper = char.isupper()
            shiftChar = chr((ord(char) + shift - ord('A' if isUpper else 'a')) % 26 + ord('A' if isUpper else 'a'))
            result += shiftChar
        else:
            result += char
    return result

def decrypt(text, shift):
    if shift == 0:
        print("Bruteforcing all shifts:")
        for i in range(1, 26):
            decrypted_text = encrypt(text, -i)
            print(f"Shift {i}: {decrypted_text}")
    else:
        return encrypt(text, -shift)

def main():
    choice = input("Choose operation:\n1. Encrypt\n2. Decrypt\nEnter choice (1 or 2): ")

    if choice == '1':
        toEncrypt = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift amount: "))
        result = encrypt(toEncrypt, shift)
        print("Encrypted text:", result)

    elif choice == '2':
        toDecrypt = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift amount (0 for bruteforce): "))
        result = decrypt(toDecrypt, shift)
        print("Decrypted text:", result)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
