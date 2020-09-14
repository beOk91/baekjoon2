min_num,max_num=map(int,input().strip().split())
arr=[True]*(max_num-min_num+1)

for j in range(max(2,int(min_num**0.5)),int(max_num**0.5)+1):
    for k in range(j*j,max_num+1,j*j):
        if k>=min_num and arr[k-min_num]:
            arr[k-min_num]=False
print(sum(1 if i else 0 for i in arr))



"""
for i in range(2,int(max_num**0.5)+1):
    for j in range(min_num,max_num+1):
        if arr[j-min_num] and j%(i*i)==0:
            arr[j-min_num]=False
print(sum(1 if i else 0 for i in arr))
"""