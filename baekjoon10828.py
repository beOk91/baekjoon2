import sys
num=int(sys.stdin.readline().strip())
stackArr=[]
for i in range(num):
    cmd=sys.stdin.readline().strip().split()
    if cmd[0]=="push":
        stackArr.append(int(cmd[1]))
    elif cmd[0]=="top":
        print(-1 if len(stackArr)==0 else stackArr[len(stackArr)-1])
    elif cmd[0]=="size":
        print(len(stackArr))
    elif cmd[0]=="empty":
        print(1 if len(stackArr)==0 else 0)
    elif cmd[0]=="pop":
        print(-1 if len(stackArr)==0 else stackArr.pop())
