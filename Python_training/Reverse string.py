d = "my name is kiran"
f = d.split()
n = []
for i in f:
    if i == "name":
        i = "name"[::-1]
        n.append(i)
    elif i == "kiran":
        i = "kiran"[::-1]
        n.append(i)
    else:
        n.append(i)
f = "       ".join(n)
print(f)
