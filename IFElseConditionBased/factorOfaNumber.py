a= int(input("Enter a number : "))

if a>0:
    print(f"Factor of {a} are:")
    for i in range (1,a+1):
        if a%i==0:
            print(i , end=" ")
else:
    print("Please enter a Positive Number")