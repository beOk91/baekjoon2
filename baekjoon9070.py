t=int(input())
for _ in range(t):
    n=int(input())
    arr=[list(map(int,input().strip().split())) for _ in range(n)]
    arr.sort(key=lambda x:(x[1]/x[0],x[0]))
    print(arr[0][1])