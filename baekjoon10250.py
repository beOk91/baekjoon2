n=int(input())
for _ in range(n):
    h,w,n=map(int,input().strip().split())
    print(n%h*100+n//h+1 if n%h!=0 else h*100+n//h)