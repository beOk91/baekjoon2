import sys,decimal
n=int(sys.stdin.readline().strip())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()
print("%d" %(round(decimal.Decimal(sum(arr))/decimal.Decimal(len(arr)))))
print(arr[len(arr)//2])
print(arr[0] if len(arr)==1 else arr[1])
print(0 if len(arr)==1 else (abs(arr[0])+abs(arr[len(arr)-1]) if arr[0]<0 and arr[len(arr)-1]>0 else abs(arr[len(arr)-1]-arr[0])))