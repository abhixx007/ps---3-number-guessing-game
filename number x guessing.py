import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts_used = 0

    print("\n--- Welcome to the Number Guessing Game ---")
    print("Guess the secret number between 1 and 100. You have 5 attempts.")

    while attempts_used < max_attempts:
        user_input = input("\nEnter your guess: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Enter a whole number.")
            print(f"Attempts left: {max_attempts - attempts_used} (no attempt lost)")
            continue

        if guess < 1 or guess > 100:
            print("Out of range. Enter a number between 1 and 100.")
            print(f"Attempts left: {max_attempts - attempts_used} (no attempt lost)")
            continue

        attempts_used += 1
        attempts_left = max_attempts - attempts_used

        if guess == secret_number:
            word = "attempt" if attempts_used == 1 else "attempts"
            print(f"Congratulations! You guessed it in {attempts_used} {word}.")
            return
        elif guess < secret_number:
            print(f"Too low! Attempts left: {attempts_left}")
        else:
            print(f"Too high! Attempts left: {attempts_left}")

    print(f"\nGame Over! The number was {secret_number}.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

main()
