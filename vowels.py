# 16. List comprehensions:
# (c) Form a list of vowels selected from a given word

elem = input("Enter any word : ")
vowels =['a','e','i','o','u']
list1=[]
for x in elem:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in given word : ",list1)