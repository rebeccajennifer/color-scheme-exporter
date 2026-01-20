# =============================================
#   Python Highlighting Showcase for VS Code
# =============================================

# ----- Imports -----
import math
import sys
from typing import List, Dict, Tuple, Any, Optional

# ----- Constants -----
PI = 3.14159
COLORS = ["red", "green", "blue"]

# ----- Enums -----
from enum import Enum, auto

class ShapeType(Enum):
    CIRCLE = auto()
    SQUARE = auto()
    TRIANGLE = auto()

# ----- Decorators -----
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

# ----- Classes, Inheritance, Properties -----
class Shape:
    """Base class for geometric shapes."""

    def __init__(self, name: str):
        self.name = name

    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")

    def __repr__(self):
        return f"<Shape name={self.name}>"

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @log_call
    def area(self) -> float:
        return PI * (self._radius ** 2)

# ----- Functions, Type Hints, Lambdas -----
def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    dx, dy = p1[0] - p2[0], p1[1] - p2[1]
    return math.sqrt(dx ** 2 + dy ** 2)

scale = lambda x, factor=1.0: x * factor  # lambda expression

# ----- Control Flow, Comprehensions, f-strings -----
def demonstrate():
    circles: List[Circle] = [Circle(r) for r in range(1, 4)]
    for i, c in enumerate(circles):
        print(f"Circle {i}: radius={c.radius:.2f}, area={c.area():.2f}")

    color_map: Dict[str, ShapeType] = {color: st for color, st in zip(COLORS, ShapeType)}
    print(f"Color map: {color_map}")

    total_area = sum(c.area() for c in circles)
    print(f"Total area = {total_area:.3f}")

    try:
        bad_circle = Circle(-1)
    except ValueError as e:
        print(f"Caught exception: {e}")

# ----- Context Manager, File I/O -----
@log_call
def save_summary(filename: str, data: Any) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for line in data:
            f.write(str(line) + "\n")

# ----- Entry Point -----
if __name__ == "__main__":
    demonstrate()
    save_summary("output.txt", ["Done", sys.version])
