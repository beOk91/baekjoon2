n=int(input())
for k in range(n):
    m=int(input())
    for i in range(m):
        for j in range(m):
            if i==0 or i==m-1:
                print("#",end="")
            elif j==0 or j==m-1:
                print("#",end="")
            else:
                print("J",end="")
        print()
    if k!=n-1:print()