import sys
n=int(sys.stdin.readline().strip())
n_list=list(map(int,sys.stdin.readline().strip().split()))
sanguen={}
for e in n_list:
    sanguen[e]=1
m=int(sys.stdin.readline().strip())
m_list=list(map(int,sys.stdin.readline().strip().split()))
for e in m_list:
    print(sanguen.get(e,0),end=" ")