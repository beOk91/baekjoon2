import sys
while True:
    text=sys.stdin.readline().rstrip()
    if text==".":break
    stack=[]
    for e in text:
        if e in ["(","["]:stack.append(e)
        elif e==")":
            if len(stack)!=0 and stack[-1]=="(":stack.pop()
            else:stack.append("no");break
        elif e=="]":
            if len(stack)!=0 and stack[-1]=="[":stack.pop()
            else:stack.append("no");break
    print("yes" if len(stack)==0 else "no")