while True:
    cmd=input().strip().split()
    if cmd[1]=="W":
        if cmd[0]=="0" and cmd[2]=="0":
            break
        elif int(cmd[0])-int(cmd[2])<-200:
            print("Not allowed")
        else:
            print(int(cmd[0])-int(cmd[2]))
    else:
        print(int(cmd[0])+int(cmd[2]))
        