import itertools
n=int(input())
arr=[i for i in range(1,n+1)]
find_n=tuple(list(map(int,input().strip().split())))
arr_list=list(itertools.permutations(arr,n))
print(arr_list[arr_list.index(find_n)+1] if arr_list.index(find_n)!=len(arr_list)-1 else -1)
