l,p=map(int,input().strip().split())
n_list=list(map(int,input().strip().split()))
print(" ".join(str(i-l*p) for i in n_list))