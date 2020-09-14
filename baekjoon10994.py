n=int(input())
for i in range(4*n-3):
    for j in range(4*n-3):
        if i==0 or j==0 or i==4*n-4 or j==4*n-4:
            print("*",end="")
        elif i%2==0 and (j==0 or j==4*n-4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

"""
1+(n-1)*4
4*n-3
1 -> 1

2- > 5

3 -> 9

4- > 13
"""