import sys
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    cnt=0
    for i in range(2,n+1):
        temp=n
        while True:
            if temp%i==0:cnt+=1;temp//=i
            else:break
    print(cnt)