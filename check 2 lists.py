# 6. Write a program to prompt the user to enter two lists of integers and check
# (a) Whether lists are of the same length.
# (b) Whether the list sums to the same value.
# (c) Whether any value occurs in both Lists.

list1 = input("Enter the first list of integers: ").split()
list2 = input("Enter the second list of integers: ").split()

list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]

if len(list1) == len(list2):
    print("The lists have the same length.")
else:
    print("The lists have different lengths.")

if sum(list1) == sum(list2):
    print("The lists have the same sum.")
else:
    print("The lists have different sums.")

common = set(list1) & set(list2)
if common:
    print("The lists have the following common elements:", common)
else:
    print("The lists have no common elements.")