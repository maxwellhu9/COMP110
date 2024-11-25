"""Dictionary Functions"""

__author__ = "730759980"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = {}
    # Loop through the original dictionary
    for key in dict1:
        value = dict1[key]
        # Check if the value already exists in the inverted dictionary
        if value in invert_dict:
            raise KeyError(f"Duplicate Key for {key}")
        # Swap the key and value
        invert_dict[value] = key
    return invert_dict


def favorite_color(dict1: dict[str, str]) -> str:
    counter: dict[str, int] = {}
    top_color = ""
    top_count = 0

    for name in dict1:
        color = dict1[name]
        # If the color already exists, increase its count
        if color in counter:
            counter[color] += 1
        else:
            counter[color] = 1

        # Check if this color has the highest count so far
        if counter[color] > top_count:
            top_color = color
            top_count = counter[color]

    return top_color


def count(list1: list[str]) -> dict[str, int]:
    dict_count: dict[str, int] = {}

    # Loop through the list and count occurrences of each string
    for i in list1:
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1

    return dict_count


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    # Loop through each word and categorize it by its first letter
    for word in list1:
        first_letter = word[0].lower()  # Convert the first letter to lowercase
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]

    return result


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    # Check if the day already exists in the dictionary
    if day in dict1:
        # Only add the student if they are not already in the list
        if student not in dict1[day]:
            dict1[day].append(student)
    else:
        # If the day doesn't exist, create a new entry with the student
        dict1[day] = [student]
