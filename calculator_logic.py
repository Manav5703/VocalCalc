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
        "/": "by"
    }

    filtered_tokens = [symbol_map.get(token, token) for token in filtered_tokens]

    # Look for addition commands
    if "add" in filtered_tokens or "plus" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("plus") - 1] if "plus" in filtered_tokens else filtered_tokens[filtered_tokens.index("add") - 1])
        y = float(filtered_tokens[filtered_tokens.index("plus") + 1] if "plus" in filtered_tokens else filtered_tokens[filtered_tokens.index("add") + 1])
        result = add(x, y)
        history_entry = f"{int(x)} + {int(y)} = {int(result)}"  # Format for history without decimals
        return result, history_entry

    # Look for subtraction commands
    elif "subtract" in filtered_tokens or "minus" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("minus") - 1] if "minus" in filtered_tokens else filtered_tokens[filtered_tokens.index("subtract") + 1])
        y = float(filtered_tokens[filtered_tokens.index("minus") + 1] if "minus" in filtered_tokens else filtered_tokens[filtered_tokens.index("subtract") - 1])
        result = subtract(x, y)
        history_entry = f"{int(x)} - {int(y)} = {int(result)}"  # Format for history without decimals
        return result, history_entry

    # Look for multiplication commands
    elif "multiply" in filtered_tokens or "times" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("times") - 1] if "times" in filtered_tokens else filtered_tokens[filtered_tokens.index("multiply") - 1])
        y = float(filtered_tokens[filtered_tokens.index("times") + 1] if "times" in filtered_tokens else filtered_tokens[filtered_tokens.index("multiply") + 1])
        result = multiply(x, y)
        history_entry = f"{int(x)} * {int(y)} = {int(result)}"  # Format for history without decimals
        return result, history_entry

    # Look for division commands
    elif "divide" in filtered_tokens or "by" in filtered_tokens:
        x = float(filtered_tokens[filtered_tokens.index("by") - 1] if "by" in filtered_tokens else filtered_tokens[filtered_tokens.index("divide") - 1])
        y = float(filtered_tokens[filtered_tokens.index("by") + 1] if "by" in filtered_tokens else filtered_tokens[filtered_tokens.index("divide") + 1])
        result = divide(x, y)
        if isinstance(result, str):
            history_entry = f"{int(x)} / {int(y)} = {result}"  # Error case
        else:
            history_entry = f"{int(x)} / {int(y)} = {result:.2f}"  # Format for history with 2 decimal points for division
        return result, history_entry

    else:
        return "Invalid command", ""  # Return an error message and an empty history entry
