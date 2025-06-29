import random

print("Welcome to the Number Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy (1–50)")
print("2. Medium (1–100)")
print("3. Hard (1–500)")

# Choosing the difficulty level now
level = input("Enter 1, 2, or 3: ")

if level == "1":
    max_range = 50
elif level == "2":
    max_range = 100
elif level == "3":
    max_range = 500
else:
    print("Invalid choice. Defaulting to Medium.")
    max_range = 100

secret_number = random.randint(1, max_range)
attempts = 0

print(f"\nI've picked a number between 1 and {max_range}. Can you guess it?")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print(" Too low!")
    elif guess > secret_number:
        print(" Too high!")
    else:
        print(f" Correct! You guessed it in {attempts} tries.")
        break
