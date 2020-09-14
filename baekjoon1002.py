t=int(input().strip())
for _ in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().strip().split())
    r3=((y2-y1)**2+(x2-x1)**2)**0.5

    print(0 if r3==0 and r1!=r2 else -1 if r3==0 and r1==r2 else 2 if r1+r2>r3 and r3>abs(r1-r2) else 1 if r1+r2==r3 or abs(r1-r2)==r3 else 0)