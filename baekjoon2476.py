n=int(input())
def f():
    dice=sorted(list(map(int,input().strip().split())))
    if len(set(dice))==1:
        return 10000+dice[0]*1000
    elif len(set(dice))==2:
        return 1000+dice[1]*100
    else:
        return dice[2]*100
print(max(f() for _ in range(n)))