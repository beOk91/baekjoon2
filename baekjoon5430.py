t=int(input().strip())
for _ in range(t):
    p=input().strip()
    p=p.replace("RR","")
    print(p)
    n=int(input().strip())
    arrText=input().strip()
    arr=[]
    if n!=0:arr=arrText.replace("[","").replace("]","").split(",")
    for e in p:
        if e=="R":arr=arr[::-1]
        elif e=="D":
            if len(arr)==0:print("error")
            else:arr.pop(0)
    if len(arr)!=0:
        print("["+",".join(e for e in arr)+"]")