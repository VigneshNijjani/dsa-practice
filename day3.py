
#roman to integer
def roman(s):
    d={"zero":0,"I":1,"V":5,"X":10,"l":50,"c":100,"D":500,"M":1000}
    total=0
    prev=0
    for i in range(len(s)-1,-1,-1):
        if d[s[i]]<prev: 
            total-=d[s[i]]
        else:
            total+=d[s[i]]
        prev=d[s[i]]
    return total
            

print(roman("III"))



# buy vs sell stocks
def stock(prices):
    i=0
    j=1
    buy=0
    sell=0
    while i<j and j<len(prices)-1:
        if prices[i+1]<prices[buy] :
            buy=i+1 
        if prices[j+1]>prices[sell]:
            sell=j+1
        i+=1
        j+=1
    if prices[buy]<prices[sell]:
        return prices[sell]-prices[buy]
    else:
        return 0

stock([7,1,2,5,6,4,3])      

#Abc
