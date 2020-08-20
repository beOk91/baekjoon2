n,m=map(int,input().strip().split())
if (n<0 and m>=0) or (n>=0 and m<0):
    print(abs(n)+abs(m))
else:
    print(max(abs(n),abs(m))-min(abs(n),abs(m)))