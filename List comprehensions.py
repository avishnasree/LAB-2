# 16. List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) Form a list ordinal value of each element of a word (Hint: use ord() to get ordinal
# values)

# (a)print positive Numbers in a List

lst = []
n = int(input("Enter size of list "))
for i in range(0, n):
    x = int(input("Enter element of list "))
    lst.append(x)

print("Positive numbers in", lst, "are: ")

for i in lst:
    if i >= 0:
        print(i, end=" ")


