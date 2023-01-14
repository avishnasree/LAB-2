# 17. Sort dictionary in ascending and descending order.


x = {'sree': 40, 'avishna': 2, 'anu': 1, 'anusree': 3}

lst = list(x.items())
lst.sort()
print('Ascending order is', lst)

lst = list(x.items())
lst.sort(reverse=True)
print('Descending order is', lst)




