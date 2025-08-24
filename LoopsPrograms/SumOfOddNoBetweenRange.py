# Take an integer A as input. You have to print the sum of all odd numbers in the range [1, 
# A]. 
# Input:- A= 4 
# Output:- 4 
# Explanation:- For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. Sum = 1 + 3 = 4.
n=int(input("enter the no : "))
sum=0
i=0
while(i<=n):
    if(i%2 !=0):
        sum=sum+i
    i=i+1
print(sum)