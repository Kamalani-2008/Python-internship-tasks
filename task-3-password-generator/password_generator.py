
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter the password length: "))

        if length < 1:
            print("Password length must be at least 1.")
            return

        password = generate_password(length)

        print("Your generated password is:", password)

    except ValueError:
        print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
