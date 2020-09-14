    n=int(input())
    arr=[]
    for _ in range(n):
        a,b=map(int,input().strip().split())
        arr.append((a,b))
    arr.sort(key=lambda x: (x[1],x[0]))
    r,k=[arr[0]],0
    for i in range(1,n):
        if arr[k][1]<=arr[i][0]:
            r.append(arr[i])
            k=i
    print(len(r))