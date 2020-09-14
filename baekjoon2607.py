import sys
n=int(sys.stdin.readline().strip())
text=list(sys.stdin.readline().strip())
arr=[0]*26
for e in text:
    arr[ord(e)-65]+=1
cnt=0
for _ in range(n-1):
    text1=list(sys.stdin.readline().strip())
    arr2=arr.copy()
    for e in text1:
        arr2[ord(e)-65]-=1
    if sum(abs(e) for e in arr2) in [0,1]:
        print(text1)
        cnt+=1
print(cnt)