import math

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y, decimal_points=2):
    """Return the quotient of x and y, handling division by zero, formatted to decimal points."""
    if y == 0:
        return "Error: Division by zero"
    return round(x / y, decimal_points)

def logarithm(x, base=10):
    """Return the logarithm of x to the specified base."""
    if x <= 0:
        return "Error: Logarithm of non-positive number"
    return round(math.log(x, base), 2)

def square_root(x):
    """Return the square root of x."""
    if x < 0:
        return "Error: Square root of negative number"
    return round(math.sqrt(x), 2)

def cube_root(x):
    """Return the cube root of x."""
    return round(math.cbrt(x), 2)

def exponentiation(x, y):
    """Return x raised to the power of y."""
    return round(x ** y, 2)

def exponential(x):
    """Return the value of e raised to the power of x."""
    return round(math.exp(x), 2)

# Trigonometric functions
def sine(x):
    """Return the sine of x (in degrees)."""
    return round(math.sin(math.radians(x)), 2)

def cosine(x):
    """Return the cosine of x (in degrees)."""
    return round(math.cos(math.radians(x)), 2)

def tangent(x):
    """Return the tangent of x (in degrees)."""
    return round(math.tan(math.radians(x)), 2)

def parse_command(command):
    """Parse the command and perform the corresponding arithmetic operation."""
    command = command.lower()
    tokens = command.split()

    # Filter out non-essential words
    filtered_tokens = [token for token in tokens if token not in ["what", "is", "the", "and", "of"]]

    symbol_map = {
        "+": "plus",
        "-": "minus",
        "*": "times",
        "/": "by",
        "^": "power",
        "sin": "sine",
        "cos": "cosine",
        "tan": "tangent",
        "√": "square_root",
    }

    filtered_tokens = [symbol_map.get(token, token) for token in filtered_tokens]

    # Look for addition commands
    if "add" in filtered_tokens or "plus" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("plus") - 1] if "plus" in filtered_tokens else filtered_tokens[filtered_tokens.index("add") - 1])
        y = float(filtered_tokens[filtered_tokens.index("plus") + 1] if "plus" in filtered_tokens else filtered_tokens[filtered_tokens.index("add") + 1])
        result = add(x, y)
        history_entry = f"{int(x)} + {int(y)} = {int(result)}"
        return result, history_entry

    # Look for subtraction commands
    elif "subtract" in filtered_tokens or "minus" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("minus") - 1] if "minus" in filtered_tokens else filtered_tokens[filtered_tokens.index("subtract") + 1])
        y = float(filtered_tokens[filtered_tokens.index("minus") + 1] if "minus" in filtered_tokens else filtered_tokens[filtered_tokens.index("subtract") - 1])
        result = subtract(x, y)
        history_entry = f"{int(x)} - {int(y)} = {int(result)}"
        return result, history_entry

    # Look for multiplication commands
    elif "multiply" in filtered_tokens or "times" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("times") - 1] if "times" in filtered_tokens else filtered_tokens[filtered_tokens.index("multiply") - 1])
        y = float(filtered_tokens[filtered_tokens.index("times") + 1] if "times" in filtered_tokens else filtered_tokens[filtered_tokens.index("multiply") + 1])
        result = multiply(x, y)
        history_entry = f"{int(x)} * {int(y)} = {int(result)}"
        return result, history_entry

    # Look for division commands
    elif "divide" in filtered_tokens or "by" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("by") - 1] if "by" in filtered_tokens else filtered_tokens[filtered_tokens.index("divide") - 1])
        y = float(filtered_tokens[filtered_tokens.index("by") + 1] if "by" in filtered_tokens else filtered_tokens[filtered_tokens.index("divide") + 1])
        result = divide(x, y)
        if isinstance(result, str):
            history_entry = f"{int(x)} / {int(y)} = {result}"  # Error case
        else:
            history_entry = f"{int(x)} / {int(y)} = {result:.2f}"
        return result, history_entry

    # Look for exponentiation commands
    elif "power" in filtered_tokens or "raised to" in filtered_tokens:
        if "power" in filtered_tokens:
            base = float(filtered_tokens[filtered_tokens.index("power") - 1])
            exponent = float(filtered_tokens[filtered_tokens.index("power") + 1])
        else:  # Handling "raised to" case
            base = float(filtered_tokens[filtered_tokens.index("raised") - 1])
            exponent = float(filtered_tokens[filtered_tokens.index("raised") + 2])
        
        result = exponentiation(base, exponent)
        history_entry = f"{int(base)} raised to the power of {int(exponent)} = {result}"
        return result, history_entry

    # Square root handling (either as "square root" or as "√")
    if "square_root" in filtered_tokens or ("square" in filtered_tokens and "root" in filtered_tokens):
        try:
            # Capture phrases like "square root of 49" or "√49"
            if "square_root" in filtered_tokens:
                x = float(filtered_tokens[filtered_tokens.index("square_root") + 1])
            else:
                x = float(filtered_tokens[filtered_tokens.index("root") + 1])
            result = square_root(x)
            history_entry = f"√({int(x)}) = {result}"
            return result, history_entry
        except (ValueError, IndexError):
            return "Error: Invalid input for square root", ""

    # Cube root handling (either as "cube root" or as "∛")
    elif "cube root" in filtered_tokens or "∛" in filtered_tokens or ("cube" in filtered_tokens and "root" in filtered_tokens):
        try:
            # Capture phrases like "cube root of 27" or "∛27"
            if "∛" in filtered_tokens:
                x = float(filtered_tokens[filtered_tokens.index("∛") + 1])
            else:
                x = float(filtered_tokens[filtered_tokens.index("root") + 1])
            result = cube_root(x)
            history_entry = f"∛({int(x)}) = {result}"
            return result, history_entry
        except (ValueError, IndexError):
            return "Error: Invalid input for cube root", ""

    # Look for logarithm commands
    elif "log" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("log") + 1])
        result = logarithm(x)
        history_entry = f"log({int(x)}) = {result}"
        return result, history_entry

    elif "sine" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("sine") + 1])
        result = sine(x)
        history_entry = f"sin({int(x)}) = {result}"
        return result, history_entry

    elif "cosine" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("cosine") + 1])
        result = cosine(x)
        history_entry = f"cos({int(x)}) = {result}"
        return result, history_entry

    elif "tangent" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("tangent") + 1])
        result = tangent(x)
        history_entry = f"tan({int(x)}) = {result}"
        return result, history_entry
    
    else:
        return "Invalid command", ""  # Return an error message and an empty history entry

