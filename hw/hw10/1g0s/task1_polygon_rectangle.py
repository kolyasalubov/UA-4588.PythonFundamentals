"""
Task 1 — Polygon → Rectangle (Inheritance)

Models a simple inheritance chain and computes a rectangle's area.
"""

from typing import Union


class Polygon:
    """Base class representing a polygon with a given number of sides."""
    
    def __init__(self, sides: int) -> None:
        """Initialize polygon with number of sides.
        
        Args:
            sides: Number of sides for the polygon
        """
        self._sides = sides
    
    def describe(self) -> str:
        """Return description of the polygon.
        
        Returns:
            String description with number of sides
        """
        return f"Polygon with {self._sides} sides"


class Rectangle(Polygon):
    """Rectangle class inheriting from Polygon."""
    
    def __init__(self, width: float, height: float) -> None:
        """Initialize rectangle with width and height.
        
        Args:
            width: Width of the rectangle
            height: Height of the rectangle
            
        Raises:
            ValueError: If width or height are not positive
        """
        super().__init__(4)  # Rectangle always has 4 sides
        
        if width <= 0:
            raise ValueError("Width must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
            
        self._width = width
        self._height = height
    
    def area(self) -> float:
        """Calculate area of the rectangle.
        
        Returns:
            Area as width * height
        """
        return self._width * self._height
    
    def perimeter(self) -> float:
        """Calculate perimeter of the rectangle.
        
        Returns:
            Perimeter as 2 * (width + height)
        """
        return 2 * (self._width + self._height)
    
    def describe(self) -> str:
        """Return detailed description of the rectangle.
        
        Returns:
            String description including sides, width, and height
        """
        return f"Rectangle with {self._sides} sides, width: {self._width}, height: {self._height}"


if __name__ == "__main__":
    # Create two rectangles with different dimensions
    rect1 = Rectangle(5.0, 3.0)
    rect2 = Rectangle(10.0, 7.5)
    
    # Print details for first rectangle
    print("Rectangle 1:")
    print(f"  {rect1.describe()}")
    print(f"  Area: {rect1.area()}")
    print(f"  Perimeter: {rect1.perimeter()}")
    print()
    
    # Print details for second rectangle
    print("Rectangle 2:")
    print(f"  {rect2.describe()}")
    print(f"  Area: {rect2.area()}")
    print(f"  Perimeter: {rect2.perimeter()}")
    print()
    
    # Demonstrate error handling
    try:
        invalid_rect = Rectangle(-1, 5)
    except ValueError as e:
        print(f"Error creating invalid rectangle: {e}")