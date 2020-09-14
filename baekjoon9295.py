n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().strip().split())
    print("Case {}: {}".format(i,a+b))