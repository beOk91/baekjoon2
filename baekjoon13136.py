r,c,n=map(int,input().strip().split())
print((r//n if r%n==0 else r//n+1)*(c//n if c%n==0 else c//n+1))