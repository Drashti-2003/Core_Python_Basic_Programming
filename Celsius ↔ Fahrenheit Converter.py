# Python Program to Convert Celsius to Fahrenheit and vice –a-versa.

# Temperature Conversion using functions (library style)

# function (like library)
def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


# user input
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    c = float(input("Enter Celsius value: "))
    print("Fahrenheit =", c_to_f(c))

elif choice == "2":
    f = float(input("Enter Fahrenheit value: "))
    print("Celsius =", f_to_c(f))

else:
    print("Invalid choice")