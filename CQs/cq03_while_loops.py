"""While Loops Challenge Question"""

__author__ = "730759980"


def num_instances(phrase: str, search_char: str) -> int:

    count = 0
    index = 0

    # Loop through the phrase character by character
    while index < len(phrase):
        # If the current character matches search_char, increment count
        if phrase[index] == search_char:
            count += 1
        # Move to the next character
        index += 1

    return count
