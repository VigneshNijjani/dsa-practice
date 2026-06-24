
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

