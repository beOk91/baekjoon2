from collections import deque
import sys
num=int(sys.stdin.readline().strip())
myQueue=deque()

for i in range(num):
    cmd=sys.stdin.readline().strip().split()
    if cmd[0]=="push":
        myQueue.append(cmd[1])
    elif cmd[0]=="front":
        print(-1 if len(myQueue)==0 else myQueue[0])
    elif cmd[0]=="size":
        print(len(myQueue))
    elif cmd[0]=="empty":
        print(1 if len(myQueue)==0 else 0)
    elif cmd[0]=="pop":
        print(-1 if len(myQueue)==0 else myQueue.popleft())
    elif cmd[0]=="back":
        print(-1 if len(myQueue)==0 else myQueue[-1])