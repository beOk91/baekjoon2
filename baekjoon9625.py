k=int(input())
ret=[1,0]
for _ in range(k):
    ret[0],ret[1]=ret[0]-ret[0]+ret[1],ret[0]+ret[1]
print(ret[0],ret[1])