"""Number Guessing Game"""

__author__ = "730759980"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
