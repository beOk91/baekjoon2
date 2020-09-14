import sys
n=int(sys.stdin.readline().strip())
n_list=[]
for _ in range(n):
    n_list.append(float(sys.stdin.readline().strip()))
n_list.pop(n_list.index(min(n_list)))
print("%.2f" %min(n_list))