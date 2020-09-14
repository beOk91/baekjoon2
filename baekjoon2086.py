a,b=map(int,input().strip().split())
fibo=[0,1,1]+[0]*(b-2)
for i in range(3,b+1):
    fibo[i]=fibo[i-1]+fibo[i-2]
print(sum(fibo[:b+1])%1000000000-sum(fibo[:a])%1000000000)