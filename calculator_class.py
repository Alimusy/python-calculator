# Calculator class with basic and advanced operations.
import math


class Calculator:
    def __init__(self):
        # Dictionary attribute: operation symbol -> function that does the work
        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": divide,
        }

    def add_operation(self, symbol, function):
        """Add a new operation symbol and its function to the dictionary."""
        self.operations[symbol] = function

    def calculate(self, num1, symbol, num2):
        """Look up the symbol in the dictionary and apply it to the numbers."""
        # Check the operation symbol is valid
        if symbol not in self.operations:
            message = f"Invalid operation '{symbol}'. Choose from: {', '.join(self.operations)}"
            print("Error:", message)
            raise ValueError(message)

        # Check both inputs are numbers (bool is excluded: True/False are not numbers here)
        for value in (num1, num2):
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                message = f"'{value}' is not a number."
                print("Error:", message)
                raise TypeError(message)

        # Run the operation; report maths errors such as dividing by zero
        try:
            return self.operations[symbol](num1, num2)
        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)
            raise


# ----- Operation functions -----
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Exponentiation: a raised to the power b."""
    return math.pow(a, b)


def square_root(a, b=None):
    """Square root of a. The second number is not used."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def logarithm(a, b):
    """Logarithm of a in base b."""
    if a <= 0:
        raise ValueError("Logarithm needs a number greater than 0.")
    if b <= 0 or b == 1:
        raise ValueError("Logarithm base must be greater than 0 and not 1.")
    return math.log(a, b)


# Operations that only use the first number
ONE_NUMBER_OPERATIONS = {"sqrt"}


def read_number(prompt):
    """Ask for a number until the user types one. Returns an int or float."""
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            pass
        try:
            return float(text)
        except ValueError:
            print(f"Error: '{text}' is not a number. Please try again.")


# ----- Main program -----
if __name__ == "__main__":
    calc = Calculator()
    calc.add_operation("^", power)
    calc.add_operation("sqrt", square_root)
    calc.add_operation("log", logarithm)

    print("Calculator")
    print("Operations:", ", ".join(calc.operations))
    print("  ^ = power, sqrt = square root, log = log of the first number in base the second")
    print("Type q as the operation to quit.")

    while True:
        symbol = input("\nOperation: ").strip().lower()
        if symbol in ("q", "quit", "exit"):
            print("Goodbye!")
            break
        if symbol not in calc.operations:
            print(f"Error: Invalid operation '{symbol}'. Choose from: {', '.join(calc.operations)}")
            continue

        num1 = read_number("First number: ")
        if symbol in ONE_NUMBER_OPERATIONS:
            num2 = 0  # not used by this operation
        else:
            num2 = read_number("Second number: ")

        try:
            result = calc.calculate(num1, symbol, num2)
            print("Result:", result)
        except (ValueError, TypeError, ZeroDivisionError):
            # calculate() already printed the error message; keep the loop going
            pass
