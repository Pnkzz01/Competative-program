#  Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
# given number N. 
# Input:- N = 1589 
# Output:- 23 
# Explanation:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.
n=int(input("enter the no : "))
sum=0
while(n>0):
    i=n%10
    sum=sum+i
    n=n//10
print(sum)