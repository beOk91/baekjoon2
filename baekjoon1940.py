import sys
n=int(sys.stdin.readline().strip())
m=int(sys.stdin.readline().strip())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
cnt=0
for i in range(n//2+1):
    if m-n_list[i] in n_list and n_list[i]!=m-n_list[i]:cnt+=1
print(cnt)