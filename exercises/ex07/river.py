"""File to define the River class."""

__author__ = "730759980"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """A River ecosystem containing Fish and Bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Initialize the River with a number of Fish and Bears."""
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    def check_ages(self):
        """Remove Fish older than 3 days and Bears older than 5 days."""
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []

        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        return None

    def bears_eating(self):
        """Simulate Bears eating Fish if there are enough Fish in the River."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove Bears with a hunger_score less than 0."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None

    def repopulate_fish(self):
        """Repopulate Fish in the River based on existing pairs."""
        for _ in range(len(self.fish) // 2):
            for _ in range(4):
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulate Bears in the River based on existing pairs."""
        for _ in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Display the current day and populations of Fish and Bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week in the River ecosystem (7 days)."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove a specified number of Fish from the River."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
