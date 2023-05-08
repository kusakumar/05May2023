"""
9.pyramid -9
given a number N write a program to print a pyramid inside a rectangle of N rows using zeros to represent the pyramid
 and dots. in the remaining places of the rectangle.
input
5
output

. . . . 0 . . . .
. . .0 0 0. . .
. . 0 0 0 0 0 . .
. 0 0 0 0 0 0 0 .
0 0 0 0 0 0 0 0 0

"""
N=int(input("Enter the value: "))
m=2*(N-1)
for i in range(0,N+1):
    for s in range(0,m):
        print(". ",end=" ")
    for s in range(0, 2*i+1):
        print("0 ",end=' ')
    for s in range(0,m):
        print(". ",end=' ')
    m-=1
    print(" ")