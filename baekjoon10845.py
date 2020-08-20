import sys
num=int(sys.stdin.readline().strip())
queueArr=[]
for i in range(num):
    cmd=sys.stdin.readline().strip().split()
    if cmd[0]=="push":
        queueArr.append(cmd[1])
    elif cmd[0]=="front":
        print(-1 if len(queueArr)==0 else queueArr[0])
    elif cmd[0]=="size":
        print(len(queueArr))
    elif cmd[0]=="empty":
        print(1 if len(queueArr)==0 else 0)
    elif cmd[0]=="pop":
        print(-1 if len(queueArr)==0 else queueArr.pop(0))
    elif cmd[0]=="back":
        print(-1 if len(queueArr)==0 else queueArr[len(queueArr)-1])