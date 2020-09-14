arr=[[0]*100 for _ in range(100)]
for _ in range(4):
    s=list(map(int,input().strip().split()))
    for i in range(s[1],s[3]):
        for j in range(s[0],s[2]):
            arr[i][j]=1

print(sum(sum(arr[i]) for i in range(100)))