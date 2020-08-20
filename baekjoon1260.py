import sys
from collections import deque
n,m,v=map(int,sys.stdin.readline().strip().split())
graphArr=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().strip().split())
    graphArr[a][b]=1
    graphArr[b][a]=1

def bfs(graph,start):
    q=deque()
    visited=[False for _ in range(len(graph))]
    q.append(v)
    visited[v-1]=True
    while len(q)!=0:
        q_data=q.popleft()
        print(q_data,end=" ")
        for i in range(1,len(graph[q_data])):
            if graph[q_data][i]==1 and not visited[i-1]:
                q.append(i)
                visited[i-1]=True    
visitedForDFS=[False]*n
def dfs(graph,start):
    if visitedForDFS[start-1]:
        return
    else:
        print(start,end=" ")
        visitedForDFS[start-1]=True
        for i in range(1,len(graph[start])):
            if graph[start][i]==1 and not visitedForDFS[i-1]:
                dfs(graph,i)

dfs(graphArr,v)
print()
bfs(graphArr,v)

"""
import queue
def bfs(graph,start):
    q=queue.Queue()
    visited=[False for _ in range(len(graph))]
    q.put(v)
    visited[v-1]=True
    while q.qsize()!=0:
        q_data=q.get()
        print(q_data,end=" ")
        for i in range(1,len(graph[q_data])):
            if graph[q_data][i]==1 and not visited[i-1]:
                q.put(i)
                visited[i-1]=True
"""