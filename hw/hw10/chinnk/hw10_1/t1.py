from __future__ import annotations
from typing import Tuple

class Polygon:
    def __init__(self, width: float, height: float) -> None:
        self.width = float(width)
        self.height = float(height)

    def sides(self) -> Tuple[float, float]:
        return self.width, self.height


class Rectangle(Polygon):
    def area(self) -> float:
        return self.width * self.height


r = Rectangle(3, 4)
print("Task1 → rectangle sides:", r.sides(), "area:", r.area())
