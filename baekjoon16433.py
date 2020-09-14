n,r,c=map(int,input().strip().split())
visited=[[True]*n for _ in range(n)]
stack=[]
stack.append((r,c))
visited[r-1][c-1]=False
while len(stack)!=0:
    (a,b)=stack.pop()
    if a-2>=0 and b-2>=0 and visited[a-2][b-2]:
        stack.append((a-1,b-1))
        visited[a-2][b-2]=False
    if a-2>=0 and b<n and visited[a-2][b]:
        stack.append((a-1,b+1))
        visited[a-2][b]=False
    if a<n and b-2>=0 and visited[a][b-2]:
        stack.append((a+1,b-1))
        visited[a][b-2]=False
    if a<n and b<n and visited[a][b]:
        stack.append((a+1,b+1))
        visited[a][b]=False
for i in range(n):
    for j in range(n):
        print("." if visited[i][j] else "v",end="")
    print()