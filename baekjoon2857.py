import sys
fbi=[]
for i in range(1,6):
    text=sys.stdin.readline().strip()
    if text.count("FBI")>0:fbi.append(i)
print(" ".join(str(e) for e in fbi) if len(fbi)!=0 else "HE GOT AWAY!")