# Python Calculator

A simple calculator function in Python.

`calculator(num1, num2)` asks for an operator (`+`, `-`, `*`, `/`), works out the result with `if / elif / else`, and returns it. It returns an error message for an invalid operator or for division by zero.

## Run

```bash
python calculator.py
```

Example:

```
Enter an operator (+, -, *, /): +
Result: 15
Enter an operator (+, -, *, /): /
Result: Error: cannot divide by zero.
```

## Calculator class

`calculator_class.py` defines a `Calculator` class that keeps its operations in a dictionary. You can add new operations with `add_operation(symbol, function)`, and `calculate(num1, symbol, num2)` checks the symbol and the numbers before it runs the operation.

Besides `+`, `-`, `*` and `/`, it adds three operations that use the `math` library:

| Symbol | Operation |
|---|---|
| `^` | power |
| `sqrt` | square root (needs one number) |
| `log` | log of the first number in the base of the second |

The program keeps asking for calculations until you type `q`.

```bash
python calculator_class.py
```
