# File: Dictionaries_in_Python.py
# Description: How to create and use Dictionaries in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Dictionaries in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Dictionaries_in_Python (date of access: XX.XX.XXXX)


# Creating an empty dictionary
a = dict()
d = {}
print(a)
print(d)

# Creating filled dictionary in form of Key --> Value
d = {'a': 101, 10: 202}
print(d)
print(d['a'])
print(d[10])

# Operations with dictionaries
print('a' in d)
print(11 not in d)
d['a'] = 102  # Reassigning value for the existing key
print(d)

# Getting the value of the element of the dictionary by the key
print(d[10])  # If there is no such key it will show mistake
print(d.get(11))  # If there is no such key it will show 'None'

# Deleting information from the dictionary
del d['a']  # It will delete the pair Key --> Value
print(d)

# Using loops for the dictionaries
a = {'A': 15, 'B': 23, 'C': 35, 'D': 43}
for x in a:
    print(x, end=' ')  # It will show keys

print()
for x in a.keys():
    print(x, end=' ')  # Again it will show keys

print()
for y in a.values():
    print(y, end=' ')  # It will show values

print()
for x, y in a.items():
    print(x, y, end='; ')  # It will show pairs Key --> Value

print()
# It is possible to store value as a list in the dictionary
print(a)
a['D'] = ['Diana', 'Rose']
print(a)
a['D'] += ['Sun']
print(a)
