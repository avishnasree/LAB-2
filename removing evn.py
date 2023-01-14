# 12. From a list of integers, create a list after removing even numbers.


list = [1, 2, 3, 4, 5]

for i  in list:
	if(i%2 == 0):
         list.remove(i)

print("list after removing even numbers:")
print (list)
