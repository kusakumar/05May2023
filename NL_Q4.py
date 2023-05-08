""""
4. numbers in rectangle-2
Given two numbers M and N write a program to print a rectangle of M rows and N columns using numbers starting from 1
input   output
M=2     1 2 3
N=3     4 5 6
"""
M=int(input("Enter the 1st value: "))
N=int(input("Enter the 2nd value: "))
c=1
for i in range(1,M+1):
    for j in range(1,N+1):
        print(c,end=' ')
        c+=1
    print()