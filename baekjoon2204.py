while True:
    n=int(input())
    if n==0:break
    m=[]
    for _ in range(n):
        m.append(input())
    m.sort(key=lambda x:x.lower()[::])
    print(m[0])