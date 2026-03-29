#program to make a simple calculator (using functions).

# Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# User Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

choice = input("Enter operator (+, -, *, /): ")

# Operation
if choice == '+':
    print(a, "+", b, "=", add(a, b))
elif choice == '-':
    print(a, "-", b, "=", sub(a, b))
elif choice == '*':
    print(a, "*", b, "=", mul(a, b))
elif choice == '/':
    print(a, "/", b, "=", div(a, b))
else:
    print("Invalid choice")