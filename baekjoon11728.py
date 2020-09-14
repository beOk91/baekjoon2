n,m=map(int,input().strip().split())
a=[]
for _ in range(2):
    a+=list(map(int,input().strip().split()))
a.sort()
print(" ".join(str(element) for element in a))