import random

def guess_number_game():
    # Generated a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I've picked a random number between 1 and 100.")
    print("Do you think you have what it takes to guess it? Let's find out!")

    while not guessed_correctly:
        # Incremented the number of attempts
        attempts += 1
        
        # Prompted user for their guess
        try:
            user_guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Whoa, that's not a number! Please enter a valid integer.")
            continue

        # Compared user guess with the generated number
        if user_guess < number_to_guess:
            print("Too low! Aim higher, my friend!")
        elif user_guess > number_to_guess:
            print("Too high! Bring it down a notch!")
        else:
            guessed_correctly = True
            print(f"\n🎉 Woohoo! You've guessed it right! The number was {number_to_guess}.")
            print(f"It took you {attempts} attempt(s) to crack the code. Well done, genius!")

    print("\nThanks for playing! Hope you had fun. Until next time, keep guessing!")

# Run the game
if __name__ == "__main__":
    guess_number_game()
