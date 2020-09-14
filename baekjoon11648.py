n=input().strip()
cnt=0
while len(n)!=1:
    new_n=1
    for e in n:
        new_n*=int(e)
    n=str(new_n);cnt+=1
print(cnt)