import sys

try:
    x = int(input("X: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Canot devided by 0")
    sys.exit(1)


print(f"{x} / {y} = {result}")
