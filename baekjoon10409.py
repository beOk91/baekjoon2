n,t=map(int,input().strip().split())
n_list=list(map(int,input().strip().split()))
sum1=0
for i in range(n):
    sum1+=n_list[i]
    if sum1>t:
        print(i)
        break
    if i==(n-1):
        print(n)
if sum1==0:
    print(0)