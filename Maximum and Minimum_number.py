#python to find out maximum and minimum number out of three user entered number.

# User Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Finding Maximum
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

# Finding Minimum
if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

# Output
print("Maximum number:", max_num)
print("Minimum number:", min_num)