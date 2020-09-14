a,d,k=map(int,input().strip().split())
print("X" if d>0 and a>k else (k-a)//d+1 if (k-a)%d==0 else "X")