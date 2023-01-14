# 9. Create a single string separated with space from two strings by swapping the character at position 1.
# Eg : str1 = “Hello” str2 =”World” , then create a string str3 = “Hollo Werld” [Hint: use slicing and concatenation ]

a= ('Hello')
b= ('World')
x= a[1]
a= a.replace(a[1],b[1],1)
b= b.replace(b[1],x,1)
print(a+' '+b)

