from datetime import datetime
price=0
totalprice=0
pricelist=[]
finalamt=0
itlist=[]
qtlist=[]
prlist=[]
user=input("enter your name:")
lists='''todays prices are........
         rice=40/kg
         sugar=30/kg
         oil=180/ltr
         dal=120/kg
         onions=20/kg
         salt=8/kg
         '''
n1=int(input('''
                SELECT THE OPTIONS
                1:TO SEE ITEMS LIST
                2:EXIT
                enter your choice:'''))
if n1==1:
    print(lists)
else:
    print("TRY TO BUY ANYTHING YOU CAN...")
ilists={"rice":40,"sugar":30,"oil":180,"dal":120,"onions":20,"salt":8}
for i in range(len(ilists)):
    n2=int(input('''After selecting one item you need to press
                    1:FOR MORE
                    0:EXIT
                    enter your choice:'''))
    if n2==0:
        break
    if n2==1:
        item=input("enter item from above list:")
        quantity=int(input("enter quantity of items:"))
        if item in ilists.keys():
            price=quantity*(ilists[item])
            pricelist.append((item,quantity,ilists,price))
            totalprice+=price
            itlist.append(item)
            qtlist.append(quantity)
            prlist.append(price)
            dis=(totalprice*10)/100
            finalamt=totalprice-dis
        else:
            print("please check the items above list")
f1=input("if you want to print bill press 1 to print 0 to no:")
if f1==1:
    pass
if finalamt!=0:
        print('''
              ==============NARI SUPERMARKET==================
                                CHITYAL  
                            CUSTOMER INVOICE''')
        print("NAME:",user,20*" ","DATE:",datetime.now())
        print(70*"-")
        print("sno",8*" ","items",3*" ","quantity",2*" ","price")
        print(70*"-")
        for i in range(len(pricelist)):
       
            print(i,8*" ",itlist[i],8*" ",qtlist[i],5*" ",3*" ",prlist[i])
            print(70*"-")
print("TOTAL PRICE=",totalprice)
print(70*"^")
print("FINAL AMOUNT=",finalamt)
print(70*"^")
print("10% discount NET SAVED=",dis)
print(70*"-")
print(25*"=","THANK YOU VISIT AGAIN",25*"=")





                    

        
