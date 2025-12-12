## 📏 Rectangle Class Definition
#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle with private instance attributes for width and height.
    Includes properties for validation and public methods for area, perimeter,
    and custom string representation.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle, with validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
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
        """
        Sets the height of the rectangle, with validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)) or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character '#'.

        Returns:
            str: The graphical representation or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Build the rectangle representation
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += '#' * self.__width
            if i < self.__height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the object that can be used to recreate it.

        Returns:
            str: A string in the format "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"

# --- Example Usage ---
# The example below shows how the class works based on the requirements,
# including the custom printing behavior.

if __name__ == "__main__":
    try:
        my_rectangle = Rectangle(2, 4)
        print("Rectangle:", my_rectangle)
        print("---")
        print(repr(my_rectangle))
        print(f"Area: {my_rectangle.area()}")
        print(f"Perimeter: {my_rectangle.perimeter()}")

        print("\n--- Testing updates ---")
        my_rectangle.width = 5
        my_rectangle.height = 3
        print("New Rectangle:", my_rectangle)
        print(f"Area: {my_rectangle.area()}")
        print(f"Perimeter: {my_rectangle.perimeter()}")

        print("\n--- Testing zero dimensions ---")
        zero_rect = Rectangle(0, 5)
        print(f"Zero Rect (print): '{zero_rect}'") # Expected empty string
        print(f"Zero Rect Area: {zero_rect.area()}")
        print(f"Zero Rect Perimeter: {zero_rect.perimeter()}")
        print(f"Zero Rect (repr): {repr(zero_rect)}")

        print("\n--- Testing validation (should raise exceptions) ---")
        try:
            Rectangle(10, "5") # TypeError for height
        except Exception as e:
            print(f"Caught expected exception: {e}")

        try:
            my_rectangle.width = -1 # ValueError for width
        except Exception as e:
            print(f"Caught expected exception: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

