# def fib( n: int) -> int:
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(2))


# def rever(s,ans=[]):
#     l=len(s)
#     if l==0:
#         return ans
#     ans.append(s[l-1])
#     return rever(s[:l-1],ans)
# print(rever("hello"))


def isPalindrome( s,l=0,r=None,list1=[]) -> bool:
    if r is None:
        list1.extend(i.lower()for i in s if i.isalnum())
        r=len(list1)-1 
    if l>r and list1[l]!=list1[r]:
        return True
    return isPalindrome(list1,l+1,r-1,list1)
    
print(isPalindrome("A man, a plan, a canal: Panama"))


# s="hello"
# l=0
# r=len(s)-1
# while l<r:
#     s[l],s[r]=s[r],s[l]
#     l+=1
#     r-=1
# print(s)