import sys
n=int(sys.stdin.readline().strip())
stack,num=[],1
ret=[]
for _ in range(n):
    n1=int(sys.stdin.readline().strip())
    while True:
        if len(stack)!=0 and stack[-1]==n1:
            stack.pop();ret.append("-");break
        else:
            if num>n:break
            stack.append(num)
            ret.append("+");num+=1
if len(ret)==n*2:print("\n".join(str(e) for e in ret))
else:print("NO")