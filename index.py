def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption & Decryption")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"\n🔐 Encrypted Message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {decrypted}")
    else:
        print("Invalid choice! Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()