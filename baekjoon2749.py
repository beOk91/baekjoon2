n=int(input().strip())
fibo=[0,1,1,2]+[0]*(n-3)
for i in range(3,n+1):
    fibo[i]=(fibo[i-1]+fibo[i-2])%1000000
print(fibo[n])