import sys
for _ in range(3):
    num=int(sys.stdin.readline().strip())
    sum1=0
    for i in range(num):
        sum1+=int(sys.stdin.readline().strip())
    print("0" if sum1==0 else "+" if sum1>0 else "-")