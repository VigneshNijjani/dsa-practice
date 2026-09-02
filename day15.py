# # recurssion
# 1.printnumber from 1 to n 

def numbers(n):
    if n==0:
        return
    print(n)
    numbers(n-1)
numbers(5)

# 2.sum of first n numbers ex: sum(5)=5+4+3+2+1=15

def add(n,sum1=0):
    if n==0:
        print(sum1)
        return
    sum1+=n
    add(n-1,sum1)
add(5)

# 3.product of first n numbers/factorial ex: factorial(5)=5*4*3*2*1=120

def product(n,pro=1):
    if n==0:
        print(pro)
        return
    pro*=n
    product(n-1,pro)
product(5)


# 4.revese a string using reccurrsion ex:reverse(hello)=olleh

def reverse1(s,ans=""):
    l=len(s)
    if l==0:
        print(ans)
        return
    ans+=s[l-1]
    reverse1(s[:l-1],ans)
reverse1("hello")


# 5.sum of digits ex:sum_od _digits(169)=1+6+9=16

def sum_of_digits(n,sum=0):
    if n==0:
        print(sum)
        return
    rem=n%10
    sum+=rem
    n//=10
    sum_of_digits(n,sum)
sum_of_digits(169)

