import sys
def f(idx,arr1,arr2):
    if idx==len(arr1):
        #arr[sum(arr2)]=True;return
    f(idx+1,arr1,arr2+[arr1[idx]])
    f(idx+1,arr1,arr2)
"""
n=int(sys.stdin.readline().strip())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
arr=[False]*(sum(n_list)+1)
f(0,n_list,[])
for i in range(1,len(arr)):
    if not arr[i]:
        print(i);break
"""

n=int(sys.stdin.readline().strip())
n_list=sorted(list(map(int,sys.stdin.readline().strip().split())))
n_sum=1
for i in range(len(n_list)):
    if n_sum<n_list[i]:
        break
    n_sum+=n_list[i]
print(n_sum)