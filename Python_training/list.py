# In python the list means the collection of various type of elements(or)heterogenous elements
# This list contains int,float,str,boolean elements
my_list = [1, 3.2, 'prasad', True]

# List methods
# append method
my_list.append(4)  # it will adding the elements
print(my_list)

# Extend method
my_list.extend([25, 26, 27])  # it will expand the list
print(my_list)

# copy method
my_list.copy()  # it will make duplicate list from original list
print(my_list)

# remove method
my_list.remove(1)  # it will remove the element by giving directly element name
print(my_list)

# pop method
my_list.pop(5)  # it will remove the element by giving index number of element
print(my_list)

# index method
# it will print index number of the element in list
print(my_list.index('prasad'))

# reverse method
my_list.reverse()  # it will reverse the list
print(my_list)

# sort method
my_list1 = [2, 1, 4, 5, 3]
my_list1.sort()  # it will arrange the list in ascending order
print(my_list1)

# descending order of sorting method
my_list1.sort(reverse=True)
print(my_list1)

# clear Method
my_list.clear()  # it will clear the entire list
print(my_list)

# List comprehensive
print([x**3 for x in [1, 3, 2, 4, 6]])
