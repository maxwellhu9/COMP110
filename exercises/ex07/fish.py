"""File to define the Fish class."""


class Fish:
    """A Fish in the river ecosystem."""

    age: int

    def __init__(self):
        """Initialize a Fish with age 0."""
        self.age = 0
        return None

    def one_day(self):
        """Simulate one day for the Fish, aging it."""
        self.age += 1
        return None
