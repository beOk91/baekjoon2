while True:
    cmd=list(map(int,input().strip().split()))
    if cmd[0]==0:break
    for i in range(1,cmd[0]+1):
        if i==1:
            print(cmd[i],end=" ")
        elif cmd[i]!=cmd[i-1]:
            print(cmd[i],end=" ")
    print("$")
