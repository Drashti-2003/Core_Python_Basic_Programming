# Python program to check if the number provided by the user is an Armstrong number.

# Example:153 = 1^3 + 5^3 + 3^3 = 153

num = int(input("Enter a number: "))

# Convert number to string to count digits
n = len(str(num))
temp = num
sum = 0

# Calculate sum of digits power n
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** n)
    temp = temp // 10

# Check Armstrong
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")