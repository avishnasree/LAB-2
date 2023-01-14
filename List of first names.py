# 5. Store a list of first names. Count the occurrences of ‘a’ within the list.

names = ["avishna", "anusree", "abhi", "anu"]
count = 0
for name in names:
    count += name.count("a")
print(count)
