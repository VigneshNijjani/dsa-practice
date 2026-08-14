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


# Step	Operation	A (8L)	B (5L)	C (3L)           
# -------------------------------------------
# 0       Start        8     0      0
# 1       A → B        3     5      0
# 2       B → C        3     2      3
# 3       C → A        6     2      0
# 4       B → C        6     0      2
# 5       A → B        1     5      2
# 6       B → C        1     4      3
# 7       C → A        4     4      0 ✅



