# Dictionary
'''
1.A dictionary is a datatype which consist of key-value pair and enclosed with curly brackets.
2.It allow all datatypes and update.
3.It is a mutuable(changable).
4.It is a key-value pairs is also called as Items.
5.It will not allowed the duplicate data.
6.It is a case-sensitive.
'''
# Program
a = {1111: 'Prasad', 'thiest': 'Devotee', 'jobless': True}  # Dictionay
print(a)  # It will print entire dictionary

# Dictionary Methods.
# copy()
print(a.copy())

# keys()
print(a.keys())

# values()
print(a.values())

# items()
print(a.items())

# get():accessing single value
print(a.get('jobless'))

# pop()
print(a.pop('thiest'))

# update()
a.update({1111: 'hero'})
print(a)


# clear()
print(a.clear())


# Tuple
'''
1.Tuple is the datatype  and closed with curve brackets.
2.Tuple is a immutuable(unchangable).
3.It is allow to duplicate.
4.It is not allow to update.
'''
# program
b = (1, 2, 3, 4, 5)
print(b)  # it will print entire tuple.

# Tuple methods
'''The tuple methods are bulit-in methods.'''

# len()
print(len(b))

# max()
print(max(b))

# min()
print(min(b))

# sum()
print(sum(b))
