n=5
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()


print()
print()
print()
print()

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

for i in range(1,n+1):
        print(" "*(n-i)+("*"*i))

for i in range(1,n+1):
        print(" "*(n-i)+("* "*i))




