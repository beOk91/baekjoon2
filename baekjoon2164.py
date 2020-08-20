from collections import deque
import sys
arr,idx=deque(),0
num=int(sys.stdin.readline().strip())
for i in range(1,num+1):
    arr.append(i)
while len(arr)!=1:
    if idx%2==0:
        arr.popleft()
    else:
        arr.append(arr.popleft())
    idx+=1

print(arr.pop())