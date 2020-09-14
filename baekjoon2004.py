import sys
n,m=map(int,sys.stdin.readline().strip().split())
val,cnt=1,0
for i in range(n,m,-1):
    val*=i
for i in range(1,n-m+1):
    val/=i
for i in str(int(val))[::-1]:
    if i=="0":cnt+=1
    else:break
print(cnt)