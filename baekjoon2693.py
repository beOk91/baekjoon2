t=int(input())
for _ in range(t):
    arr=sorted(list(map(int,input().strip().split())),reverse=True)
    print(arr[2])