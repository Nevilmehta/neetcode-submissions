from collections import Counter
from typing import List

class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (x2, y2), count in self.points.items():
            # need a different x and y, with equal horizontal/vertical distance
            if abs(x2 - x) == 0 or abs(x2 - x)!=abs(y2 - y):
                continue

            side = abs(x2 - x)

            # check the two possible fourth corners
            total += count * self.points[(x, y2)] * self.points[(x2, y)]

        return total