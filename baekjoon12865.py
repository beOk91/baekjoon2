n,k=map(int,input().strip().split())
goods_list=[]

for _ in range(n):
    goods_weight,goods_value=list(map(int,input().strip().split()))
    goods_list.append((goods_weight,goods_value))
memory=[[0]*(k+1) for _ in range(n+1)]

def put_goods(idx,weight):
    if memory[idx][weight]!=0:
        return memory[idx][weight]
    if idx==len(goods_list):
        return 0
    n1=0
    if weight+goods_list[idx][0]<=k:
        n1=goods_list[idx][1]+put_goods(idx+1,weight+goods_list[idx][0])
    n2=put_goods(idx+1,weight)
    memory[idx][weight]=max(n1,n2)
    return memory[idx][weight]

print(put_goods(0,0))





