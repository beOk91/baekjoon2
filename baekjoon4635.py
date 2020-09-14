while True:
    n=int(input())
    if n==-1:
        break
    result,previous_t=0,0
    for _ in range(n):
        s,t=map(int,input().strip().split())
        result+=((t-previous_t)*s)
        previous_t=t
    print(str(result) +" miles")