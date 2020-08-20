n=int(input())
n_list=list(map(int,input().strip().split()))
n_list.sort()
if len(n_list)%2==0:
    print(n_list[0]*n_list[len(n_list)-1])
else:
    print(n_list[len(n_list)//2]**2)