n,m=map(int,input().strip().split())
k_list=list(map(int,input().strip().split()))
num=[False]*(n+1)
for element in k_list:
    for i in range(element,n+1,element):
        if not num[i]:
            num[i]=True
print(sum(i if num[i] else 0 for i in range(n+1)))