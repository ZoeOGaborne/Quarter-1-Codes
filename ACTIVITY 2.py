import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x_sq = math.sqrt((pow(x2 - x1, 2) + (pow(y2 - y1, 2))))

print(f"The distance between the two points is {round(x_sq, 2)}")