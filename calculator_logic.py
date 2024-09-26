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
    command = command.lower()
    tokens = command.split()
    
    # Example parsing logic
    if "plus" in tokens:
        x = int(tokens[tokens.index("plus") - 1])
        y = int(tokens[tokens.index("plus") + 1])
        return add(x, y)
    elif "subtract" in tokens:
        x = int(tokens[tokens.index("subtract") + 1])
        y = int(tokens[tokens.index("subtract") - 1])
        return subtract(y, x)
    elif "multiply" in tokens:
        x = int(tokens[tokens.index("multiply") - 1])
        y = int(tokens[tokens.index("multiply") + 1])
        return multiply(x, y)
    elif "divide" in tokens:
        x = int(tokens[tokens.index("divide") - 1])
        y = int(tokens[tokens.index("divide") + 1])
        return divide(y, x)
    else:
        return "Invalid command"
