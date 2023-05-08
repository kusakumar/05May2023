""""
5. half pyramid-2

write a program to print the number in the given N number of rows in the following half pyramid pattern

input
5
out put
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
N=int(input("Enter the value: "))
c=1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(c,end=' ')
        c+=1
    print()