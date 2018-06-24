'''
Created on 01-Jun-2016

@author: BALASUBRAMANIAM
'''
a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
print(type(a_set))
a_set = {1, 2}
a_set.add(4)
print(a_set)

a_set = {1, 2, 3}
print(a_set)
a_set.update({2, 4, 6})
print(a_set)

a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
print(a_set)

print(a_set.pop())

a_set = {1, 2, 3}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set=a_set.union(b_set)

print(a_set)

a_set = {1, 2, 3}
a_set=a_set.intersection(b_set)
print(a_set)
a_set = {1, 2, 3}
b_set = {1,2,3,4,5,6}
a_set = b_set.difference(a_set)
print(a_set)

a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
print(a_set.issubset(b_set))