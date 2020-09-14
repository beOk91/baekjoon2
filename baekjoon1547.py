m=int(input())
cup=[1,0,0,0]
for _ in range(m):
    cmd=list(map(int,input().strip().split()))
    cup[cmd[0]-1],cup[cmd[1]-1]=cup[cmd[1]-1],cup[cmd[0]-1]
print(cup.index(1)+1)