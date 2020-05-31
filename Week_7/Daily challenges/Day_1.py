def ceasar_cypher():
    choice = input("Do you want to encrypt or decrypt?")
    text = input("Enter your message: ")
    step = int(input("Enter your step: "))

    result = ""

    if choice == 'encrypt':
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + step-65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + step - 97) % 26 + 97)

        return result
    elif choice == 'decrypt':
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - step-65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - step-97) % 26 + 97)

        return result


print(ceasar_cypher())
