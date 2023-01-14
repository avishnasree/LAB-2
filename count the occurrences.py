# 7. Write a Python program to count the occurrences of each word in a line of text.
# Hint: use split() function and dictionary
# Sample input : the quick brown fox jumps over the lazy dog
# Output : {'the': 2, 'jumps': 1, 'brown': 1, 'lazy': 1, 'fox': 1, 'over': 1, 'quick': 1, 'dog.': 1}

text = "the quick brown fox jumps over the lazy dog"

words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)