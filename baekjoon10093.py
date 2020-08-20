a,b=map(int,input().strip().split())
print(0 if max(a,b)-min(a,b)-1<0 else max(a,b)-min(a,b)-1)
print(" ".join(str(i) for i in range(min(a,b)+1,max(a,b))))