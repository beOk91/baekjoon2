import sys
n=int(sys.stdin.readline().strip())
arr=[]
for _ in range(n):
    arr.append(sys.stdin.readline().strip())
arr=list(set(arr))
arr.sort()
arr.sort(key=lambda x:len(x))
for element in arr:
    print(element)