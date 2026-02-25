import random

print("WELCOME TO NUMBER GUESSING GAME")
print("Guess a number between 1 and 50")

number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == number:
        print("Yes! Correct Guess 🎉")
        print("You guessed the number in", attempts, "attempts.")
        break

    elif guess > number:
        print("Too High! Try again.")

    else:
        print("Too Low! Try again.")