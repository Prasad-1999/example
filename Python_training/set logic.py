# Set program logic with membership operation(in).
a = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 1, 2]
b = []
for i in a:
    if i in b:
        b.remove(i)
    else:
        b.append(i)
print(b)
