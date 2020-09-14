"""
import sys
sys.setrecursionlimit(1000000)
t_list=[0,1,2,4]+[0]*(1000001-3)
def f(n):
    if t_list[n]!=0:return t_list[n]
    else:
        t_list[n]=(f(n-1)+f(n-2)+f(n-3))%1000000009
        return t_list[n]
t=int(sys.stdin.readline().strip())
for _ in range(t):
    num=int(sys.stdin.readline().strip())
    print(f(num))
"""
import sys
t_list=[0,1,2,4]+[0]*(1000001-3)
for i in range(4,1000001):
    t_list[i]=(t_list[i-1]+t_list[i-2]+t_list[i-3])%1000000009
t=int(sys.stdin.readline().strip())
for _ in range(t):
    num=int(sys.stdin.readline().strip())
    print(t_list[num])