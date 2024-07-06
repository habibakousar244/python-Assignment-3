# Take Trinangle side measurments with input method from user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Create conditional statement
if side1 == side2 == side3:
        print("It is Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
        print("It is Isosceles Triangle")
else:
        print("It is Scalene Triangle")