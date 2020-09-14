from collections import deque
import sys
n=int(sys.stdin.readline().strip())
d=deque()
for _ in range(n):
    arr=sys.stdin.readline().strip().split()
    if arr[0]=="push_front":
        d.insert(0,int(arr[1]))
    elif arr[0]=="push_back":
        d.append(int(arr[1]))
    elif arr[0]=="pop_front":
        print(d.popleft() if len(d)!=0 else -1)
    elif arr[0]=="pop_back":
        print(d.pop() if len(d)!=0 else -1 )
    elif arr[0]=="size":
        print(len(d))
    elif arr[0]=="empty":
        print(1 if len(d)==0 else 0)
    elif arr[0]=="front":
        print(d[0] if len(d)!=0 else -1)
    elif arr[0]=="back":
        print(d[len(d)-1] if len(d)!=0 else -1)
