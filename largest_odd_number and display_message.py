# program which will allow user to enter 10 numbers and display largest oddnumber from them. It will display appropriate message in case if no odd number is found.

largest_odd = None

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))

    if num % 2 != 0:   # check odd number
        if largest_odd is None or num > largest_odd:
            largest_odd = num

# Output
if largest_odd is not None:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number found")