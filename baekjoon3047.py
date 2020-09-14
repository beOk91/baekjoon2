abc=sorted(list(map(int,input().strip().split())))
a,b,c=abc[0],abc[1],abc[2]
text=list(input().strip())
arr=[]
for e in text:
    if e=="A":arr+=[a]
    elif e=="B":arr+=[b]
    elif e=="C":arr+=[c]
print(" ".join(str(e) for e in arr))