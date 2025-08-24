#WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.
a=int(input("enter the number between 1-7:"))
if a==1:
    print("Day is Sunday")
elif a==2:
    print("day is Monday")
elif a==3:
    print("day is Tuesday")
elif a==4:
    print("day is Wednesday")
elif a==5:
    print("day is Thursday") 
elif a==6:
    print("day is Friday")  
elif a==7:
    print("day is Saturday")
else:               
    print("Enter A invalid Number")