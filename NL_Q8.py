"""
8. solid half diamond
given an integer N, write a program to print the solid half diamond pattern in (2*N-1) rows and N columns similar to the pattern shown below

input
5
output
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*    """

N=int(input("Enter the value: "))
for i in range(1,N+1):
    print("* "*i)
    if i==N:
        for j in range(N-1 , 0, -1):
            print("* "*j)
    #print()