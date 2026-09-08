
def strStr(haystack: str, needle: str) -> int:
    h=haystack
    n=needle
    l=len(n)
    flag=0
    for i in range(len(h)):
        if h[i]==n[0]:
            a=i
            b=0
            if flag==0:
                temp=i+1
            while l!=0:
                if h[a]==n[b]:
                    a+=1
                    b+=1
                    l-=1
                    flag=1
                else:
                    flag=0
    if flag:
        return temp-1
    else:
        return -1


print(strStr("leetcode","leeto"))


print(200000/12)


def majorityElement(nums) -> int:
    d={}
    temp=0
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if d[i]>temp:
            temp=i
    return temp
print(majorityElement([2,2,2,1,1,1,2,2,2]))



print(2019%1000)
print(2019//1000)
print((19+1)+1000*(2-1))