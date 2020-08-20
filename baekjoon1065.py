n=int(input())
cnt=n
for i in range(1,n+1):
    val=[int(i) for i in list(str(i))]
    if len(val)==1 or len(val)==2:
        continue
    else:
        difference=val[1]-val[0]
        for j in range(1,len(val)-1):
            if difference!=(val[j+1]-val[j]):
                cnt-=1
                break

print(cnt)