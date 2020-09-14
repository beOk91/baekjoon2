import sys
n=int(sys.stdin.readline().strip())
arr=[0]*2
for _ in range(n):
    a,b=map(int,sys.stdin.readline().strip().split())
    if a>b:arr[0]+=1
    elif a<b:arr[1]+=1
print(arr[0],arr[1])