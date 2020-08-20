n=int(input())
for _ in range(n):
    car=int(input())
    opt_cnt=int(input())
    opt_total=0
    for _ in range(opt_cnt):
        opt_1,opt_price=map(int,input().strip().split())
        opt_total+=(opt_1*opt_price)
    print(car+opt_total)