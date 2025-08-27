import art
import random

print(art.logo)

# Generate any random number from 1 to 100
random_generated_number = int(random.randint(1, 100))

# Set guesses left based on difficulty level
difficulty_choice = input("Do you want to set the game level to easy or hard? Type 'easy' or 'hard': \n").lower()
guesses_left = 10 if difficulty_choice == "easy" else 5 if difficulty_choice == "hard" else 0

# If user entered invalid difficulty then guesses_left will be 0
while guesses_left == 0:
    difficulty_choice = input("Oops, I didn't understand that. Please type 'easy' or 'hard': \n").lower()
    guesses_left = 10 if difficulty_choice == "easy" else 5 if difficulty_choice == "hard" else 0

while guesses_left > 0:
    print(f"You have {guesses_left} attempts remaining.")

    try:
        guess_number = int(input("Guess a number from 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Make sure guess_number falls in range 1 to 100
    if not (1 <= guess_number <= 100):
        print("Please choose a number between 1 and 100.")
        continue

    # Compare guess_number to random_generated_number
    if guess_number == random_generated_number:
        print(f"Congrats! You guessed it right. The number was {random_generated_number}.")
        break
    elif guess_number < random_generated_number:
        print("Too low. Try a higher number.")
    else:
        print("Too high. Try a lower number.")

    guesses_left -= 1

    # If out of guesses
    if guesses_left == 0:
        print(f"Game over! The number was {random_generated_number}.")
