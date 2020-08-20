testcase=int(input())
for _ in range(testcase):
    m,n,k=map(int,input().strip().split())
    arr=[[0]*m for i in range(n)]
    visited=[[False]*m for i in range(n)]
    cnt=0
    for _ in range(k):
        a,b=map(int,input().strip().split())
        arr[b][a]=1
    q=[]
    for y in range(n):
        for x in range(m):
            if arr[y][x]==1 and not visited[y][x]:
                q.append((x,y))
                visited[y][x]=True
                while q:
                    x1,y1=map(int,q.pop())
                    visited[y1][x1]=True
                    if x1+1<m and arr[y1][x1+1]==1 and not visited[y1][x1+1]:
                        q.append((x1+1,y1))
                    if y1+1<n and arr[y1+1][x1]==1 and not visited[y1+1][x1]:
                        q.append((x1,y1+1))
                    if x1-1>=0 and arr[y1][x1-1]==1 and not visited[y1][x1-1]:
                        q.append((x1-1,y1))
                    if y1-1>=0 and arr[y1-1][x1]==1 and not visited[y1-1][x1]:
                        q.append((x1,y1-1))
                cnt+=1
    print(cnt)