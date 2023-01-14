# 2. Accept an integer n and compute n+nn+nnn.[Hint : n = 5, then compute 5 + 55 + 555]

n=int(input("Enter a number,n="))
nn=n*10+n
nnn=n*100+nn
print("n+nn+nnn=",n+nn+nnn)