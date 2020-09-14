import math,sys
n=int(sys.stdin.readline().strip())
n_list=list(map(int,sys.stdin.readline().strip().split()))
gcd_val=math.gcd(n_list[0],n_list[1])
for i in range(1,gcd_val+1):
    flag=True
    for j in range(n):
        if n_list[j]%i==0: continue
        else:
            flag=False;break
    if flag:print(i)