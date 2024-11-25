"""Plan a Cozy Tea Party"""

__author__: str = "730759980"


def main_planner(guests: int) -> None:
    """Plan and print the details for the tea party"""
    # Print a welcome message including the number of guests.
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Assume everyone at the tea party will need two tea bags"""
    # Calculate total number of tea bags by multiplying people by 2.
    return people * 2


def treats(people: int) -> int:
    """Assume for each tea a guest drinks, thy will also want 1.5 treats"""
    # Calculate total number of treats needed based on the number of tea bags.
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Assumes a cost of $0.5 per tea bag and $0.75 per treat"""
    # Compute cost of tea bags and treats
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
