n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().strip().split())
    print("Scenario #{}:".format(i))
    print(b*(b+1)//2-abs(a)*(abs(a)+1)//2 if a<0 else b*(b+1)//2-(a-1)*a//2)
    print()