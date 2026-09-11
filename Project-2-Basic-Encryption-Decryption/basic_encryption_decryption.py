def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            number = ord(char) - ord("A")
            shifted_number = (number + shift) % 26
            encrypted_char = chr(shifted_number + ord("A"))
            encrypted_text += encrypted_char

        elif char.islower():
            number = ord(char) - ord("a")
            shifted_number = (number + shift) % 26
            encrypted_char = chr(shifted_number + ord("a"))
            encrypted_text += encrypted_char

        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            number = ord(char) - ord("A")
            shifted_number = (number - shift) % 26
            decrypted_char = chr(shifted_number + ord("A"))
            decrypted_text += decrypted_char

        elif char.islower():
            number = ord(char) - ord("a")
            shifted_number = (number - shift) % 26
            decrypted_char = chr(shifted_number + ord("a"))
            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    return decrypted_text


text = input("Enter text: ")
shift = int(input("Enter shift key: "))

encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("\nOriginal text:", text)
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
