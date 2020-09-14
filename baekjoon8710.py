k,w,m=map(int,input().strip().split())
print((w-k)//m if (w-k)%m==0 else (w-k)//m+1)