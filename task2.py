# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.
sum=0
for num in range(1,51):
    sum+=num
print("total sum of the number from 1 to 50 is {}".format(sum))