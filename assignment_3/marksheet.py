# Ask name through input
name = input("enter your name: ")

# Ask marks through input
english = int(input("Enter your ENGLISH marks: "))
urdu = int(input("Enter your URDU marks: "))
maths = int(input("Enter your MATHS marks: "))
sci = int(input("Enter your SCIENCE marks: "))
com = int(input("Enter your COMPUTER marks: "))

# Add all subjects marks
total_obtained_marks = english+urdu+maths+sci+com

# Calculate percentage
percen = total_obtained_marks/500*100

# printing Marksheet format
print("==========Marksheet Of", name, "===========")
print("     MARKS OBTAINED (ENGLISH)    : ", english)
print("     MARKS OBTAINED (MATHS)      : ", maths)
print("     MARKS OBTAINED (URDU)       : ", urdu)
print("     MARKS OBTAINED (SCIENCE)    : ", sci)
print("     MARKS OBTAINED (COMPUTER)   : ", com)
print("=========== Total obtained marks : ", total_obtained_marks)
print("=========== Your total marks     : 500")
print("=========== Overall Percentage   :",percen)

# create conditional program
if percen >= 80:
    print("********You achieved A+ Grade**********")
elif percen >= 70 and percen <= 79:
    print("********You achieved A Grade**********")
elif percen >= 60 and percen <= 69:
    print("********You achieved B Grade**********")  
elif percen >= 50 and percen <= 59:
    print("********You achieved C Grade**********")
elif percen >= 40 and percen <= 49:
    print("********You achieved D Grade**********")
elif percen <= 39:
    print("********You are FAIL**********")
else:
    print("********Please enter right Marks!**********")


