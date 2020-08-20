def f(n,k):
    if n<k:
        return 0
    else:
        return n+1+f(n-k+1,k)
n,k=map(int,input().strip().split())
print(f(n,k))