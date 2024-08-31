import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    8
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")

    # Get user inputs
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)

        # Display the result
        print(f"Generated Password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    8
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")

    # Get user inputs
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)

        # Display the result
        print(f"Generated Password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
