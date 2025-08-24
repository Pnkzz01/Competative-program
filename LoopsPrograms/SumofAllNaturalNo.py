# Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
# input from user 
# Input:- N = 10 
# Output:- 55
n=int(input("enter the no : "))
sum=0
while(n>0):
    sum=sum+n
    n=n-1
print(sum)