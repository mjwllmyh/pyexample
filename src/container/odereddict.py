from collections import OrderedDict

d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
# dictionary sorted by key
print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
# dictionary sorted by value
print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))
