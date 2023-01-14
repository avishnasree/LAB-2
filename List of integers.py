# 4. Write a program to prompt the user for a list of integers. For all values greater than 100,store ‘over’ instead.

lst =  []
x = 1
while x > 0 :
    y = int(input("Enter the digit = "))
    if y > 100:
        a = "Over"
    else:
        a = y
    lst.append(a)
    print(lst)