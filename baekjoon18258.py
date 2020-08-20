import sys
num=int(sys.stdin.readline().strip())
queueArr,frontIndex,backIndex=[],0,-1

for i in range(num):
    cmd=sys.stdin.readline().strip().split()
    if cmd[0]=="push":
        queueArr.append(cmd[1])
        backIndex+=1
    elif cmd[0]=="front":
        print(-1 if frontIndex>backIndex else queueArr[frontIndex])
    elif cmd[0]=="size":
        print(len(queueArr)-frontIndex)
    elif cmd[0]=="empty":
        print(1 if frontIndex>len(queueArr) else 0)
    elif cmd[0]=="pop":
        if frontIndex>backIndex:
            print(-1)
        else:
            print(queueArr[frontIndex])
            frontIndex+=1
    elif cmd[0]=="back":
        print(-1 if frontIndex>backIndex else queueArr[backIndex])
    print(queueArr[frontIndex:])