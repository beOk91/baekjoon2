adrian=["A","B","C"]
bruno=["B","A","B","C"]
goran=["C","C","A","A","B","B"]
n=int(input().strip())
answer=input().strip()
ret=[0,0,0]
for i in range(n):
    if adrian[i%len(adrian)]==answer[i]:
        ret[0]+=1
    if bruno[i%len(bruno)]==answer[i]:
        ret[1]+=1
    if goran[i%len(goran)]==answer[i]:
        ret[2]+=1
maxVal=max(ret)
print(maxVal)
if ret[0]==maxVal:print("Adrian")
if ret[1]==maxVal:print("Bruno")
if ret[2]==maxVal:print("Goran")
