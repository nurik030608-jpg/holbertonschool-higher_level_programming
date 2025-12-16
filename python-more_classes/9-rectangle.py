#!/usr/bin/python3
"""
This is a required module-level docstring.
It describes the 4-rectangle module and the Rectangle class.
"""
class Rectangle:
    """
    Defines a rectangle with width and height properties.
    Includes features like instance tracking, a custom print symbol,
    a static method for comparison, and a class method factory for squares.
    """

    # Public class attribute 1: Tracks the number of live instances
    number_of_instances = 0
    # Public class attribute 2: Symbol used for string representation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the instance counter.

        Args:
            width (int): The width of the rectangle (must be >= 0).
            height (int): The height of the rectangle (must be >= 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation (int, >= 0)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation (int, >= 0)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character(s)
        stored in self.print_symbol.
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol) 
        
        rect_str = ""
        for i in range(self.__height):
            rect_str += symbol * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Returns a string representation that can be used with eval() to recreate
        a new instance: Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Finalizer: Called when an instance is deleted.
        Prints the specified message and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangle instances and returns the one with the largest area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: rect_1 if area(rect_1) >= area(rect_2), otherwise rect_2.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance where width == height == size.

        Args:
            cls: The class itself (Rectangle in this case).
            size (int): The length of the sides of the square (default is 0).

        Returns:
            Rectangle: A new instance of Rectangle initialized as a square.
        """
        return cls(size, size)
