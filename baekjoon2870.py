n=int(input().strip())
arr=[]
for _ in range(n):
    text=input().strip();s=""
    for element in text:
        if element.isnumeric():s+=element
        else:
            if len(s)!=0:arr.append(int(s));s=""
    if len(s)!=0:arr.append(int(s))
arr.sort()
print("\n".join(str(e) for e in arr)) 