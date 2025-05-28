name=input("enter your name")
n=int(input("no of items"))
phn=int(input("enter phn number"))
list=[]
sum=0
GST=0
total_amount=0
a='''Coffee Shop
    MENU
    Americano     85
    Caramel       90
    Cappuccino    100
    Coffee Jelly  90
    Latte         90
    Strawberry Cream 80
    Mochaccino    50
    Vanilla Bean  40
    Long Black    60
    Milkshake     80
    Flat White    50
    Milk Tea      20 '''
print(a)
dic={"americano"    :85,
    "caramel"       :90,
    "cappuccino"    :100,
    "coffee jelly"  :90,
    "latte"         :90,
    "strawberry cream" :80,
    "mochaccino"    :50,
    "vanilla bean"  :40,
    "long black"    :60,
    "milkshake"     :80,
    "flat white"    :50,
    "milk tea"      :20}
#for rep in range(len(dic)):
for i in range(n):
    order=input("what do you want from list sir")
    list.append(order)
    price=dic[order]
    sum=sum+price
print(price)
    
gst=(sum)*5/100
GST+=gst
total_amount=sum+GST
amount=int(input("costumer amount"))
change=amount-total_amount
print(("=")*50,"CAFE",("=")*50)
print("NAME:",name,(" ")*50,"PHONE NUMBER",phn)
print("LIST OF ITEMS")
for ord in list:
    print(ord)
print("TOTAL NO.OF ITEMS YOU SELECTED :",n)
print(("=")*105)
print("TOTAL COFFEE AMOUNT=",sum,(" ")*50,"GST:",GST)
print("TOTAL AMOUNT=",total_amount,(" ")*50,"COUSTEMER AMOUNT=",amount)
print("REMAINING CHANGE=",change)
print(("-")*50,"THANKS FOR VISTING",("-")*50)