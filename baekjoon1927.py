n=int(input())
arr=[]
for _ in range(n):
    cmd=int(input())
    if cmd==0:
        print(0 if len(arr)==0 else arr.pop(arr.index(min(arr))))
    else:
        arr.append(cmd)