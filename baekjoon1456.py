a,b=map(int,input().strip().split())
sosu=[False,False]+[True]*(b-1)
almost_sosu=[False]*(b+1)
for i in range(2,b+1):
    for j in range(i+i,b+1,i):
        if sosu[j]:sosu[j]=False

for i in range(a,b+1):
    if sosu[i]:
        n=2
        while True:
            if i**(n-1)<=b/i:
                almost_sosu[i**n]=True;n+=1
            if i**(n-1)>b/i:break

print(sum(1 if almost_sosu[i] else 0 for i in range(a,b+1)))