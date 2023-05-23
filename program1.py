p1 = input("enter the product")
q1 = int(input("enter the quantity"))
p1 = int(input("enter the price"))
t1 = q1*p1
print(t1)
p2 = input("enter the product")
q2 = int(input("enter the quantity"))
p2 = int(input("enter the price"))
t2 = q2*p2
print(t2)
p3 = input("enter the product")
q3 = int(input("enter the quantity"))
p3 = int(input("enter the price"))
t3 = q3*p3
print(t3)
total = t1+t2+t3
print(total)
if total>200:
    total=total-10
    print("flat 10 discount")   
elif q1>10||q2>10||q3>10:
    t1 = t1*5/100
    t2 = t2*5/100
    t3 = t3*5/100
    print("bulk 5 discount")
elif q1>20||q2>20||q3>20:
    t1 = t1*10/100
    t2 = t2*10/100
    t3 = t3*10/100
    print("bulk 10 discount")   
elif (q1>30||q2>30||q3>30)&&(q1>15||q2>15||q3>15):
    t1 = t1*50/100
    t2 = t2*50/100
    t3 = t3*50/100
    print("tiered 50 discount")
else:
    print("Please enter correct data")    
gift1 = q1*1
gift2 = q2*1
gift3 = q3*1
totalgift = gift1+gift2+gift3
totalqtypack = (q1+q2+q3)/10
tgprice = totalqtypack*5
grandtotal = total+totalgift+tgprice


