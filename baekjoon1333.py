n,l,d=map(int,input().strip().split())
i=1
while True:
    if (l+5)*i-5<=(d+1)*i-1 and (d+1)*i-1<=(l+5)*i:
        print((d+1)*i-1)
        break
    i+=1