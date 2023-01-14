# 10. Write a python program to read two lists color-list1 and color-list2. Print out all colors
# from color-list1 not contained in color-list2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green","Black"])

print(color_list_1.difference(color_list_2))
