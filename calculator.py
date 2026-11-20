# Simple calculator: asks for an operator and applies it to two numbers.


def calculator(num1, num2):
    """Ask the user for an operator and return the result of num1 <op> num2.

    Returns an error message (a string) if the operator is invalid
    or if the user tries to divide by zero.
    """
    operator = input("Enter an operator (+, -, *, /): ").strip()

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: cannot divide by zero."
        return num1 / num2
    else:
        return f"Error: '{operator}' is not a valid operator. Use +, -, * or /."


# Call the function with two numbers and print the result
result = calculator(10, 5)
print("Result:", result)

# Dividing by zero is handled too (choose / when asked)
result = calculator(10, 0)
print("Result:", result)
