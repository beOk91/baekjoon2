n,m=map(int,input().strip().split())
num=0
while n*m!=num:
    if num%4==0 and num!=0:
        print()
    num+=1
    print(num,end=" ")