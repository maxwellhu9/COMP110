"""EX03 - Wordle - Word Guessing Game"""

__author__ = "730759980"

# Define constants for the emojis used
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(expected_length: int) -> str:
    """
    Prompt the user to input a guess of the correct length.
    """
    guess = input(f"Enter a {expected_length}-character word: ")

    # Make sure the user's guess has the same number of characters as the secret word
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """
    Checks if the given single character is present anywhere in the secret word.
    """
    assert (
        len(char_guess) == 1
    )  # Make sure this function is only used with single characters

    for char in secret_word:
        if char == char_guess:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """
    Return an emoji string representing how close the guess is to the secret word.
    """
    assert len(guess) == len(
        secret
    )  # Make sure the guess and secret are the same length

    emoji_result = ""  # Initialize the string to store the emoji results

    # Compare each character in the guess to the secret word
    for idx in range(len(guess)):
        if guess[idx] == secret[idx]:
            # If the guessed character is exactly correct (same position)
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            # If the character is in the word but in the wrong position
            emoji_result += YELLOW_BOX
        else:
            # If the character is not in the word at all
            emoji_result += WHITE_BOX

    return emoji_result


def main(secret_word: str) -> None:
    """
    Main game loop where the user is given 6 attempts to guess the secret word.
    """
    turns_taken = 1  # Track the number of turns taken
    max_turns_allowed = 6  # Set the maximum number of attempts to 6

    # Run the game loop for up to 6 turns
    while turns_taken <= max_turns_allowed:
        print(f"=== Turn {turns_taken}/{max_turns_allowed} ===")

        # Get a guess from the user and ensure it has the right length
        user_guess = input_guess(len(secret_word))

        # Print the emojified feedback on the user's guess
        print(emojified(user_guess, secret_word))

        # Check if the user guessed the word correctly
        if user_guess == secret_word:
            print(f"You won in {turns_taken}/{max_turns_allowed} turns!")
            return  # Exit the game as the user has won

        turns_taken += 1  # Increment the turn counter if the guess was incorrect

    # If all turns are used up, display a failure message
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
