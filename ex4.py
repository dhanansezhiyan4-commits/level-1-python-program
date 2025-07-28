print("dhana supermarket")
print("no 44,hehru street puducherry")
print("-----------------------------")
print("bill recipt")
print("-------------------------------")
sl=int(input("enter the serial number"))
pr=(input("enter the particulars"))
rate=int(input("enter the rate"))
qty=int(input("enter the quantity"))
total=rate*qty
print("total amount",total)
gst=total*10/100
print("gst(10%)",gst)
paid=total+gst
print("amount to be paid rs",paid)
