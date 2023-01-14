# 13. Count the number of characters (character frequency) in a string.

test_str = "Wellcome"

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


print(str(all_freq))
