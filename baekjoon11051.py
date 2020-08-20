n,k=map(int,input().strip().split())
result=1
for i in range(n,n-k,-1):
    result*=i
for j in range(k,0,-1):
    result//=j
print(result%10007)