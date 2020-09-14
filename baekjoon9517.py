k=int(input().strip())
n=int(input().strip())
cnt,flag,bomb_person=0,False,0
for _ in range(n):
    cmd=input().strip().split()
    cnt+=int(cmd[0])
    if cnt>=210 and not flag:
        bomb_person=k;flag=True
    if cmd[1]=="T":k=k+1 if k+1!=9 else 1
print(bomb_person)