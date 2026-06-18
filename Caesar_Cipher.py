def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            result += chr(
                (ord(char) - base + shift) % 26 + base
            )
        else:
            result += char

    return result


def decrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            result += chr(
                (ord(char) - base - shift) % 26 + base
            )
        else:
            result += char

    return result


message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Text:", decrypted)