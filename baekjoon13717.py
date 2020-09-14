n=int(input())
poke_list=[]
poke_evol_cnt=[]
for _ in range(n):
    name=input().strip()
    poke_list.append(name)
    candy1,candy2=map(int,input().strip().split())
    evol_cnt=0
    while candy1<=candy2:
        evol_cnt+=candy2//candy1
        candy2=candy2%candy1+ (candy2//candy1*2)
    poke_evol_cnt.append(evol_cnt)
print(sum(poke_evol_cnt))
print(poke_list[poke_evol_cnt.index(max(poke_evol_cnt))])