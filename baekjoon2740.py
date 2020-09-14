n,m=map(int,input().strip().split())
arr1=[[0]*m for _ in range(n)]
for i in range(n):
    arr1[i]=list(map(int,input().strip().split()))
m,k=map(int,input().strip().split())
arr2=[[0]*k for _ in range(m)]
for i in range(m):
    arr2[i]=list(map(int,input().strip().split()))
print("\n".join(" ".join(str(sum(a*b for a,b in zip(arr1_row,arr2_col))) for arr2_col in zip(*arr2)) for arr1_row in arr1))