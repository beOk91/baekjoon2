n=int(input())
cnt=0
for i in range(1,n+1):
    if i<=99:
        cnt+=1
    else:
        val=list(map(int,str(i)))
        if val[1]-val[0]==val[2]-val[1]:
            cnt+=1
print(cnt)