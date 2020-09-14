"""풀이1
import sys,itertools
n,m=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
print("\n".join(" ".join(str(i) for i in element) for element in list(itertools.product(n_list,repeat=m))))
"""
"""#풀이2
import sys
def f(limit,arr,arr2):
    if len(arr2)==limit:
        print(" ".join(str(element) for element in arr2));return
    for i in range(len(arr)):
        f(limit,arr,arr2+[arr[i]])
n,m=map(int,sys.stdin.readline().strip().split())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
f(m,n_list,[])
"""