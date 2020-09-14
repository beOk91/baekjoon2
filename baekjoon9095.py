import sys
t=int(sys.stdin.readline().strip())
t_list=[1,2,4]+[0]*8
for _ in range(t):
    num=int(sys.stdin.readline().strip())
    for i in range(3,num):
        t_list[i]=t_list[i-1]+t_list[i-2]+t_list[i-3]
    print(t_list[num-1])