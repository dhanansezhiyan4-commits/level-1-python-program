print("government of tamilnadu")
print("electricity board")
print("-----------------------")
no1=input("enter the EB-NO:")
no2=input("enter the customer name:")
pre=int(input("reading for peuious month:"))
cur=int(input("reading for current month:"))
total=cur-pre
print("total unit consuned:",total)
paid=total*5
print("amount to be paid rs",paid)
