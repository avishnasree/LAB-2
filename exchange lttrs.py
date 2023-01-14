# 3. Create a string from the given string where the first and last character are exchanged.Eg: Python ⇒ nythoP


def exchange(string):
    first_letter = string[0]
    last_letter = string[-1]

    exchange_string = last_letter + string[1:-1] + first_letter
    print(exchange_string)

exchange("Python")