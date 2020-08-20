import math,sys
arr=[0]*100000000
arr[1],arr[2]=1,1
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        if arr[n]!=0:
            return arr[n]
        else:
            arr[n]=arr[n-1]+arr[n-2]
            return arr[n]

n=int(sys.stdin.readline().strip())
mySum=0
for i in range(1,n+1):
    for j in range(1,n+1):
        mySum+=math.gcd(fibo(i),fibo(j))
print(mySum%1000000007)