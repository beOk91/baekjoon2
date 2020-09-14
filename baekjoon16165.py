import sys
n,m=map(int,sys.stdin.readline().strip().split())
girl_group=[]
for _ in range(n):
    name=sys.stdin.readline().strip()
    cnt=int(sys.stdin.readline().strip())
    members=[]
    for _ in range(cnt):
        members.append(sys.stdin.readline().strip())
    members.sort()
    girl_group.append([name]+members)
for _ in range(m):
    name=sys.stdin.readline().strip()
    quiz=int(sys.stdin.readline().strip())
    if quiz==1:
        for element in girl_group:
            if name in element:
                print(element[0])
    else:
        for element in girl_group:
            if name in element:
                print("\n".join(str(mem) for mem in element[1:]))
