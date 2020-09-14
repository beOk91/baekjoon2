alpha=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
n,m=map(int,input().strip().split())
a,b=input().strip().split()
arr=[[0]*(n+m) for _ in range(n+m-1)]
for i in range(min(n,m)):
    arr[0][i*2]=alpha[ord(a[i])-65]
for i in range(min(n,m)):
    arr[0][i*2+1]=alpha[ord(b[i])-65]
for i in range(min(n,m)*2,n+m):
    arr[0][i]=alpha[ord(a[i-min(n,m)])-65] if n>m else alpha[ord(b[i-min(n,m)])-65]
for i in range(1,(n+m)-1):
    for j in range(i,n+m):
        arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])%10
print("{}%".format(int("".join(str(element) for element in arr[n+m-2]))))