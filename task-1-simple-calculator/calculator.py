
import secrets
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Ensure the password contains each character type.
    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    all_chars = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Fill the remaining positions securely.
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))

    # Securely shuffle the characters.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=== Secure Password Generator ===")

    try:
        length = int(input("Enter password length (minimum 4): "))

        password = generate_password(length)
        print("Generated password:", password)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
