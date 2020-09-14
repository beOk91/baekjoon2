import sys
text=list(sys.stdin.readline().strip())
idx=len(text)
n=int(sys.stdin.readline().strip())
for _ in range(n):
    cmd=sys.stdin.readline().strip().split()
    if cmd[0]=="P":
        text=text[0:idx]+[cmd[1]]+text[idx:]
        idx+=1
    elif cmd[0]=="L":
        if idx!=0:
            idx-=1
    elif cmd[0]=="D":
        if idx!=len(text):
            idx+=1
    elif cmd[0]=="B":
        if idx!=0:
            text=text[0:idx-1]+text[idx:]
            idx-=1
print("".join(element for element in text))