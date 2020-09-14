n=int(input())
n_list=list(map(int,input().strip().split()))
n_list.sort()
print(" ".join(str(e) for e in n_list))