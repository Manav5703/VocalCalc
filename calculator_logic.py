def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, handling division by zero."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

def parse_command(command):
    """Parse the command and perform the corresponding arithmetic operation."""
    # Convert the command to lowercase and split into tokens
    command = command.lower()
    tokens = command.split()

    # Filter out non-essential words like "what", "is", "the"
    filtered_tokens = [token for token in tokens if token not in ["what", "is", "the", "and"]]

    # Normalize math symbols to corresponding words
    symbol_map = {
        "+": "plus",
        "-": "minus",
        "*": "times",
        "/": "by"
    }
    
    # Replace any symbol with corresponding word
    filtered_tokens = [symbol_map.get(token, token) for token in filtered_tokens]

    # Look for addition commands
    if "add" in filtered_tokens or "plus" in filtered_tokens:
        x = int(filtered_tokens[filtered_tokens.index("plus") - 1] if "plus" in filtered_tokens else filtered_tokens[filtered_tokens.index("add") - 1])
        y = int(filtered_tokens[filtered_tokens.index("plus") + 1] if "plus" in filtered_tokens else filtered_tokens[filtered_tokens.index("add") + 1])
        return add(x, y)

    # Look for subtraction commands
    elif "subtract" in filtered_tokens or "minus" in filtered_tokens:
        x = int(filtered_tokens[filtered_tokens.index("minus") - 1] if "minus" in filtered_tokens else filtered_tokens[filtered_tokens.index("subtract") + 1])
        y = int(filtered_tokens[filtered_tokens.index("minus") + 1] if "minus" in filtered_tokens else filtered_tokens[filtered_tokens.index("subtract") - 1])
        return subtract(x, y)

    # Look for multiplication commands
    elif "multiply" in filtered_tokens or "times" in filtered_tokens:
        x = int(filtered_tokens[filtered_tokens.index("times") - 1] if "times" in filtered_tokens else filtered_tokens[filtered_tokens.index("multiply") - 1])
        y = int(filtered_tokens[filtered_tokens.index("times") + 1] if "times" in filtered_tokens else filtered_tokens[filtered_tokens.index("multiply") + 1])
        return multiply(x, y)

    # Look for division commands, ensuring "by" is treated as division
    elif "divide" in filtered_tokens or "by" in filtered_tokens:
        x = int(filtered_tokens[filtered_tokens.index("by") - 1] if "by" in filtered_tokens else filtered_tokens[filtered_tokens.index("divide") - 1])
        y = int(filtered_tokens[filtered_tokens.index("by") + 1] if "by" in filtered_tokens else filtered_tokens[filtered_tokens.index("divide") + 1])
        return divide(x, y)

    else:
        return "Invalid command"
