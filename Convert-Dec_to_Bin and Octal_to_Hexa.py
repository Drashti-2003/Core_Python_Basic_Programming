# Program to convert Decimal to Binary, Octal and Hexadecimal

num = int(input("Enter a decimal number: "))

# Conversion
binary = bin(num)
octal = oct(num)
hexa = hex(num)

# Output
print("Binary value:", binary)
print("Octal value:", octal)
print("Hexadecimal value:", hexa)