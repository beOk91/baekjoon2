import sys
cnt=1
while True:
    text=sys.stdin.readline().strip()
    if text=="Was it a cat I saw?":break
    result=""
    for i in range(0,len(text),cnt+1):
        result+=text[i]
    print(result)
    cnt+=1