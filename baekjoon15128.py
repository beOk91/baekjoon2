p1,q1,p2,q2=map(int,input().strip().split())
print(1 if (p1/q1*p2/q2*0.5)%1==0 else 0)