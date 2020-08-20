num=int(input())
for i in range(num):
    for j in range(num):
        print("*" if j%2==0 else " ",end="")
    print()
    for j in range(num):
        print(" " if j%2==0 else "*",end="")
    print()