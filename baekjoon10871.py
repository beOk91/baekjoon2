n,x=map(int,input().strip().split())
n_list=list(map(int,input().strip().split()))
for element in n_list:
    if element<x:
        print(element,end=" ")