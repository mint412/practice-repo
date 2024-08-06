import numpy as np
def add(value1, value2):
    return value1 + value2

def subtract(value1, value2):
    return value1 - value2

def divide(value1, value2):
    if value2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return value1 / value2

def multiply(value1, value2):
    return value1 * value2

def remainder(value1, value2):
    if value2 == 0:
        raise ZeroDivisionError("Cannot compute remainder when dividing by zero!")
    return value1 % value2

def calculator():
    print("Welcome to the basic calculator program!")
    try:
        num1 = float(input("Enter a numeric value: "))
        num2 = float(input("Enter another numeric value: "))
        operator = input("Enter arithmetic operator to use (+, -, /, *, %): ")

        if operator == "+":
            print("The sum is:", add(num1, num2))
        elif operator == "-":
            print("The difference is:", subtract(num1, num2))
        elif operator == "/":
            print("The quotient is:", divide(num1, num2))
        elif operator == "*":
            print("The product is:", multiply(num1, num2))
        elif operator == "%":
            print("The remainder is:", remainder(num1, num2))
        else:
            print("ERROR: Enter valid arithmetic operator...")
    except ValueError:
        print("ERROR: Enter numeric values only!")

if __name__ == "__main__":
    calculator()
