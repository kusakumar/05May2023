"""
6.numbers in square-3
given a number N write a program to print a square of N rows using numbers starting from 1 (note there is a space after every Number)
input
4
output
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""
N=int(input("Enter the value: "))
c=1
for i in range(1,N+1):
    for j in range(1,N+1):
        print(c,end=' ')
        c+=1
    print()
