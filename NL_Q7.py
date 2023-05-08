"""
7.pythagoras triplets
given a number N write a program to print the count of pythagorean triplets containing numbers A,B,C from 1 to N such that sum of quares of the numbers a and b is equal to c to the square of c where a<b<c
 input
5
output
1
"""
N=int(input("Enter the number: "))
count=0
for a in range(1,N+1):
    for b in range (a+1,N+1):
        for c in range (b+1,N+1):
            if ((a*a)+(b*b)==(c*c)):
                count+=1
print(count)