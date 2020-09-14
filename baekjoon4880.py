while True:
    cmd=list(map(int,input().strip().split()))
    if cmd[0]==0 and cmd[1]==0 and cmd[2]==0:
        break
    if (cmd[0]+cmd[2])/2==cmd[1]:
        print("AP %d" %(cmd[2]+(cmd[1]-cmd[0])))
    else:
        print("GP %d" %(cmd[2]*(cmd[1]//cmd[0])))