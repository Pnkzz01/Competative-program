#  You are given an integer A, you need to find and return the sum of all the even numbers 
# between 1 and A. Even numbers are those numbers that are divisible by 2. 
# Input:- A = 5 
# Output:- 6 
# Explanation:- Even numbers between [1, 5] are (2, 4).
n=int(input("enter the no : "))
i=0
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)