#  Write a program to print all even numbers from 1 to N, where you have to take N as input 
# from the user. 
# Input:- N = 10 
# Output:- 2 4 6 8 10
n=int(input("enter the no : "))
i=1
while(i<=n):
    if(i%2==0):
        print(i)
    i=i+1