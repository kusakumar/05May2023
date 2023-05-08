"""
1.print prime number from 1 to N
"""

n=int(input("Enter the Number :"))
for i in range(1,n+1):
    fact=0
    for j in range(1,i+1):
        if (i%j==0):
            fact+=1
    if fact==2:
        print(i,"is prime number")

#Method:2
print()
k=int(input("Enter the number: "))
for i in range (1,k+1):
    if i>1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i, "is a prime number")