n=int(input())
cnt=0
for _ in range(n):
    text=input()
    arr=[]
    arr.append(text[0])
    if len(text)==1:
        cnt+=1
    else:
        for i in range(1,len(text)):
            if text[i-1]!=text[i]:
                if text[i] not in arr:
                    arr.append(text[i])
                else:
                    break
            if i==len(text)-1:
                cnt+=1
            
print(cnt)