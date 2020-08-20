n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2-1):
        if i==n:
            print("*",end="")
        else:
            if j==0 or j==i*2-2:
                print("*",end="")
            else:
                print(" ",end="")
    print()