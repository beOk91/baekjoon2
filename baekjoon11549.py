num=int(input())
num_list=list(map(int,input().strip().split()))
cnt=0
for element in num_list:
    if element==num:
        cnt+=1
print(cnt)