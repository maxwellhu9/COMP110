"""File to define the Bear class."""


class Bear:
    """A Bear in the river ecosystem."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a Bear with age 0 and hunger_score 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulate one day for the Bear, aging it and decreasing hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase the Bear's hunger score by the number of fish eaten."""
        self.hunger_score += num_fish
