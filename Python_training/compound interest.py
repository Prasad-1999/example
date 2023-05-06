# The compund interest problem solution
P = int(input("Enter the P value:"))
r = int(input("Enter the r value:"))
n = int(input("Enter the n value:"))
t = int(input("Enter the t value:"))
A = P*1+r/n**n*t
print(A)
