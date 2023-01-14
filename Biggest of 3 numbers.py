# 1. Find biggest of 3 numbers entered.


num1 = 5
num2 = 55
num3 = 33


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
