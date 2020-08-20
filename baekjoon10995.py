n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(" ",end="")
    for j in range(n*2):
        print("*" if j%2==0 else " ",end="")
    print()