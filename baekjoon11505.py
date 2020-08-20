import sys
n,m,k=map(int,sys.stdin.readline().strip().split())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))
result=1
for element in arr:
    result*=element
for _ in range(k):
    while True:
        a,b,c=map(int,sys.stdin.readline().strip().split())
        if a==2:
            result2=1
            for i in range(b-1):
                result2*=arr[i]
            print(result//result2%1000000007)
            break
        else:
            result=result//arr[b-1]*c
            arr[b-1]=c
            