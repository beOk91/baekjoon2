n,t,c,p=map(int,input().strip().split())
print(n//t*c*p if n%t!=0 else (n//t-1)*c*p)