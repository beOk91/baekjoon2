import sys
"""
def f(idx,arr,arr2):
    if len(arr2)==3:
        m_list.append(sum(arr2))
    if idx==len(arr):
        return
    f(idx+1,arr,arr2+[arr[idx]])
    f(idx+1,arr,arr2)
"""
n,m=map(int,sys.stdin.readline().strip().split())
n_list=list(map(int,sys.stdin.readline().strip().split()))
maxval=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if maxval<=(n_list[i]+n_list[j]+n_list[k]) and (n_list[i]+n_list[j]+n_list[k])<=m:
                maxval=n_list[i]+n_list[j]+n_list[k]
print(maxval)    
"""
m_list=[]
f(0,n_list,[])
m_list=[m_list[i] for i in range(len(m_list)) if m_list[i]<=m]
print(max(m_list))
"""