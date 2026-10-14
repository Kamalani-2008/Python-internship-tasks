
import random

def main():
    print("=== Number Guessing Game ===")
    print("Guess a number between 1 and 100!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Choose a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it!")
            print("Number of attempts:", attempts)
            break

if __name__ == "__main__":
    main()
