n=int(input())
n_list=sorted(set(list(map(int,input().strip().split()))))
print(" ".join(str(element) for element in n_list))