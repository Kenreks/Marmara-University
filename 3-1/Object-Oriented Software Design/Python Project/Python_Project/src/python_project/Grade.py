import math
import random


class Grade:
    # Instead of creating grader class grade can be deal with random grading mechanism.
    # May hold course object to calculate credit * letter_grade
    _letter_map = {
        100: "AA", 95: "AA",
        90: "AA", 85: "BA",
        80: "BB", 75: "CB",
        70: "CC", 65: "CC",
        60: "DC", 55: "DC",
        50: "DD", 45: "FD",
        0: "FF"
    }
    _credit_map = {
        "AA":4.00,
        "BA":3.50,
        "BB":3.00,
        "CB":2.50,
        "CC":2.00,
        "DC":1.50,
        "DD":1.00,
        "FD":0.50,
        "FF":0.00,
    }

    def __init__(self):
        self.assign_random_grade()

    # May be computed property
    @property
    def success_grade(self):
        return self.YIS * 0.6 + self.YSS * 0.4

    @property
    def letter_grade(self):
        try:
            if self.round() < 45:
                return self._letter_map[0]
            return self._letter_map[self.round()]
        except KeyError:
            print("Letter grade not found")

    def round(self):
        return int(math.floor(self.success_grade / 5) * 5)

    def generate_random_grade(self):
        random_grade = random.randint(0, 50)
        if random_grade <= 1:
            return random.randint(0, 45)
        else:
            return random.randint(45, 101)

    def assign_random_grade(self):
        self.YIS = self.generate_random_grade()
        self.YSS = self.generate_random_grade()
        self.grade = self._credit_map[self.letter_grade]