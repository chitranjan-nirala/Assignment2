# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
from traceback import print_tb

num = int(input("enter a number:"))
if num%2==0:
    print("{} is an even number.".format(num))
else:
    print("{} is an odd number.".format(num))