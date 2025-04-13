"""
Calculator model for basic and scientific operations.
"""

import math
from typing import Union


class Calculator:
    """Calculator class for performing mathematical operations."""

    @staticmethod
    def add(x: float, y: float) -> float:
        """Return the sum of x and y."""
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        """Return the difference of x and y."""
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """Return the product of x and y."""
        return x * y

    @staticmethod
    def divide(x: float, y: float, decimal_points: int = 2) -> Union[float, str]:
        """Return the quotient of x and y, handling division by zero, formatted to decimal points."""
        if y == 0:
            return "Error: Division by zero"
        return round(x / y, decimal_points)

    @staticmethod
    def logarithm(x: float, base: float = 10) -> Union[float, str]:
        """Return the logarithm of x to the specified base."""
        if x <= 0:
            return "Error: Logarithm of non-positive number"
        return round(math.log(x, base), 2)

    @staticmethod
    def square_root(x: float) -> Union[float, str]:
        """Return the square root of x."""
        if x < 0:
            return "Error: Square root of negative number"
        return round(math.sqrt(x), 2)

    @staticmethod
    def cube_root(x: float) -> float:
        """Return the cube root of x."""
        # Handle negative numbers correctly for cube root
        if x < 0:
            return -round(abs(x) ** (1/3), 2)
        return round(x ** (1/3), 2)

    @staticmethod
    def exponentiation(x: float, y: float) -> float:
        """Return x raised to the power of y."""
        return round(x ** y, 2)

    @staticmethod
    def exponential(x: float) -> float:
        """Return the value of e raised to the power of x."""
        return round(math.exp(x), 2)

    @staticmethod
    def sine(x: float) -> float:
        """Return the sine of x (in degrees)."""
        return round(math.sin(math.radians(x)), 2)

    @staticmethod
    def cosine(x: float) -> float:
        """Return the cosine of x (in degrees)."""
        return round(math.cos(math.radians(x)), 2)

    @staticmethod
    def tangent(x: float) -> float:
        """Return the tangent of x (in degrees)."""
        return round(math.tan(math.radians(x)), 2)

    @classmethod
    def format_result(cls, result: Union[float, str]) -> str:
        """Format the result for display."""
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)
