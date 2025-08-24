#  You are given two integers A and B. You have to find the value of A^B. 
# Input:- A = 2 , B = 3 
# Output:- 8 
# Explanation:- For A=2 and B=3, the value of 2^3 = 2 * 2 * 2 = 8.
a=int(input("enter the no : "))
b=int(input("enter the power : "))
pow=1
while(b>0):
    pow=pow*a
    b=b-1
print(pow)