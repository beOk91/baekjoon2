import sys
from collections import deque
n1=int(sys.stdin.readline().strip())
n2=int(sys.stdin.readline().strip())
arr=[[0]*(n1+1) for _ in range(n1+1)]
for i in range(n2):
    a,b=map(int,sys.stdin.readline().strip().split())
    arr[a][b]=1
    arr[b][a]=1

q=deque()
q.append(1)
visited=[False]*n1
visited[0]=True
virus_com_count=0
while len(q)!=0:
    virus_Computer=q.popleft()
    virus_com_count+=1
    for i in range(1,len(arr[virus_Computer])):
        if arr[virus_Computer][i]==1 and not visited[i-1]:
            q.append(i)
            visited[i-1]=True
print(virus_com_count-1)