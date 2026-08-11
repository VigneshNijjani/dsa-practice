# # choclates

# amount=int(input("enter the amount you have :"))
# choclate_price=15
# print("number of choclates you can buy is :",amount//choclate_price)
# print("remaining amount :",amount%choclate_price)


# # current_bill
# # first 10 units ---->price 5
# # from 11 to 50 units ---->price 10
# # from 50 units to remaining ---->price 12


# price=0

# units=int(input("enter number of units :"))
# unit_price=list(map(int,input("enter unit prices \n example 5 10 12 :").split()))

# d={"ten":unit_price[0],"fifty":unit_price[1],"remaining":[2]}


# def ten(n):
#     return n*d["ten"]

# def fifty(n):
#     rem=n-10
#     return 10*d["ten"]+rem*d["fifty"]

# def remaining(n):
#     ten=10
#     n=n-10
#     fifty=40
#     rem=units-40
#     return ten*d["ten"]+fifty*d["fifty"]+rem*d["remaining"]


# if units<=10:
#     print(ten(units))
# elif units<=50:
#     print(fifty(units))
# else:
#     print(remaining(units))




## automorphic number
# number=int(input("enter your number : "))
# temp=number
# sq_num=temp*temp
# count=0
# while temp!=0:
#     temp=temp//10
#     count+=1
# if sq_num%(10**count)==number:
#     print("automorphic number")
# else:
#     print("not an automorphic number")