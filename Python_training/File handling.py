# File handling:
'''
The file handling means the file functions are open,write,read,close,append the information to file.
'''
# File functions:
'''
1.read:to read the read the entire the entire file.
2.write:to write the entire the entire file.
3.append:to add the information without overridden the file.
'''

# Program:
file = open('demo.txt', mode="r")
content = file.read()
print(content)
file.close()

# program:
file = open('demo.txt', mode="w")
file.write('''This is my file2''')
file.close()
