n=int(input().strip())
n_list=list(map(int,input().strip().split()))
cluster=int(input().strip())
total=0
for e in n_list:
    if e>0 and cluster>e:total+=cluster
    elif cluster<e:total+=(e//cluster+1)*cluster
print(total)