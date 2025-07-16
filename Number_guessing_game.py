import random

secret_number = random.randint(1, 100)
attempts = 0

print("🥳🎯 Welcome to the Number Guessing Game")
print("Guess the number I am thinking of (between 1 to 100).")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("❗ Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess > secret_number:
            print("Too high! Try a lower number.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print(f"🎊 Congratulations 🎊! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("⚠️ Please enter a valid number.")
