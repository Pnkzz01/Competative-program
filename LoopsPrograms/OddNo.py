# Write a program to print all odd numbers from 1 to N, where you have to take N as input 
# from user. 
# Input:- N = 10
# Output:- 1 3 5 7 9
n=int(input("enter the no : " ))
i=1
while(i<=n):
    if(i%2 != 0):
        print(i)
    i=i+1