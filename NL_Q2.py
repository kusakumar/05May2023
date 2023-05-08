"""
2.print the prime number from M to N
M=2
N=10
"""

m=int(input("Enter the Number1 : "))
n=int(input("Enter the number2 : "))
for i in range(m,n+1):
    fact=0
    for j in range(1,i+1):
        if (i%j==0):
            fact+=1
    if fact==2:
        print(i,"is prime number")

