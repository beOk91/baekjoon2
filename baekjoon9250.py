n=int(input())
s=[]
for _ in range(n):
    s.append(input().strip())
q=int(input())
for _ in range(q):
    text=input().strip()
    flag=False
    for i in range(n):
        if s[i] in text:
            flag=True
    if flag:
        print("YES")
    else:
        print("NO")        