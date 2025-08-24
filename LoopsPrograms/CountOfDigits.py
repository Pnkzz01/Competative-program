# Take an integer N as input and print the count of digits of that number. 
# Input:- N = 10101 
# Output:- 5 
# Explanation:- 10101 has 5 digits 
n=int(input("enter the no : "))
count=0
while(n>0):
    n=n//10
    count=count+1    
print(count)