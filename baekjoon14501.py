n=int(input())
n_list=[[0]*2 for _ in range(n)]
for i in range(n):
    n_list[i]=list(map(int,input().strip().split()))
cache=[-1]*n
def solve(day):
    if day>=n:
        return 0
    ret=0
    if cache[day]!=-1: return cache[day]
    if day + n_list[day][0]<=n:
        ret=solve(day+n_list[day][0])+n_list[day][1]
    cache[day]= max(ret,solve(day+1))
    return max(ret,solve(day+1))
print(solve(0))

"""
profit=[]
def f(day,arr,arr2):
    if day==len(arr):
        profit.append(sum(arr2))
    if day>=len(arr):
        return
    f(day+arr[day][0],arr,arr2+[arr[day][1]])
    f(day+1,arr,arr2)
f(0,n_list,[])
print(max(profit))
"""