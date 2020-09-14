n=int(input())
arr=[[""]*n for _ in range(n)]
for i in range(n):
    arr[i]=list(input().strip().split())
k=int(input())
if k==1:
    print("\n".join("".join(arr[i][j] for j in range(len(arr[i]))) for i in range(len(arr))))
elif k==2:
    print("\n".join("".join(arr[i][j][::-1] for j in range(len(arr[i]))) for i in range(len(arr))))
elif k==3:
    print("\n".join("".join(arr[::-1][i][j] for j in range(len(arr[i]))) for i in range(len(arr))))
