# 8. Get a string from an input string where all occurrences of the first character are replaced
# with ‘$’, except the first character. [eg: onion -> oni$n]

def change_char(str1):
    char = str1[0]
    length = len(str1)
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1


print(change_char('onion'))