n,p,h=map(int,input().strip().split())
previous=p
for _ in range(n):
    a=int(input())
    if previous>a:print("NTV: Dollar dropped by {} Oshloobs".format(previous-a))
    elif a>h and previous<a:print("BBTV: Dollar reached {} Oshloobs, A record!".format(a))    
    previous=a