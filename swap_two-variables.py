# program in python to swap two variables without using temporary variable.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Swapping
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)