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
    return round(x ** (1/3), 2)

def exponentiation(x, y):
    """Return x raised to the power of y."""
    return round(x ** y, 2)

def exponential(x):
    """Return the value of e raised to the power of x."""
    return round(math.exp(x), 2)

def parse_command(command):
    """Parse the command and perform the corresponding arithmetic operation."""
    command = command.lower()
    tokens = command.split()

    # Filter out non-essential words
    filtered_tokens = [token for token in tokens if token not in ["what", "is", "the", "and"]]

    symbol_map = {
        "+": "plus",
        "-": "minus",
        "*": "times",
        "/": "by",
        "^": "power"
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

    # Look for square root commands
    elif "square root" in filtered_tokens or "sqrt" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("square") + 2] if "square" in filtered_tokens else filtered_tokens[filtered_tokens.index("sqrt") + 1])
        result = square_root(x)
        history_entry = f"√({int(x)}) = {result}"
        return result, history_entry

    # Look for cube root commands
    elif "cube root" in filtered_tokens or "cbrt" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("cube") + 2] if "cube" in filtered_tokens else filtered_tokens[filtered_tokens.index("cbrt") + 1])
        result = cube_root(x)
        history_entry = f"∛({int(x)}) = {result}"
        return result, history_entry

    # Look for logarithm commands
    elif "log" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("log") + 1])
        result = logarithm(x)
        history_entry = f"log({int(x)}) = {result}"
        return result, history_entry

    # Look for exponential commands
    elif "exponential" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("exponential") + 1])
        result = exponential(x)
        history_entry = f"e^{int(x)} = {result}"
        return result, history_entry

    else:
        return "Invalid command", ""  # Return an error message and an empty history entry

