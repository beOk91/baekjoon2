t=int(input())
for _ in range(t):
    candy,cnt=map(int,input().strip().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(candy//cnt,candy%cnt))