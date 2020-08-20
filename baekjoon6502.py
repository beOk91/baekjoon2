cnt=0
while True:
    arr=input().strip().split()
    if arr[0]=="0":
        break
    else:
        cnt+=1
        print("Pizza {} ".format(cnt),end="")
        
        if int(arr[0])*2>=(int(arr[1])**2+int(arr[2])**2)**0.5:
            print("fits on the table.")
        else:
            print("does not fit on the table.")
            