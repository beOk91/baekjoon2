text=input().strip()
r,c,k=0,0,0
for i in range(int(len(text)**0.5),0,-1):
    if len(text)%i==0:r=i;c=len(text)//r;break
arr=[[""]*c for _ in range(r)]
for i in range(c):
    for j in range(r):
        arr[j][i]=text[k];k+=1
print("".join("".join((str(element2) for element2 in element)) for element in arr))