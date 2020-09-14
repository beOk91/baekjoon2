a,b,c=map(int,input().strip().split())
print(max(a/1000*b//c*1000,a/1000//b*c*1000))