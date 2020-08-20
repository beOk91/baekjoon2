num=int(input())
for i in range(num,0,-1):
    for _ in range(num-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()
for i in range(2,num+1):
    for _ in range(num-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()