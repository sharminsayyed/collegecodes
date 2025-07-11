'''
Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200,'d':400}
Sample output: ({'a': 400, 'b': 400,'d': 400, 'c': 300})
'''

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1.keys())

for key in d2.keys():
    if key in d1.keys():
        d1[key] += d2[key]
    else:
        d1[key] = d2[key]

print(d1)