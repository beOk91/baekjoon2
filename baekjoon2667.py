n=int(input())
arr=[[0]*n for _ in range(n)]
visited=[[False]*n for _ in range(n)]
result=[]
for i in range(n):
    arr[i]=list(input().strip())
for i in range(n):
    for j in range(n):
        if arr[i][j]=="1" and not visited[i][j]: 
            myStack=[]
            cnt=0
            myStack.append((i,j))
            visited[i][j]=True
            while len(myStack)!=0:
                x,y=myStack.pop(0)
                cnt+=1
                if x-1>=0 and arr[x-1][y]=="1" and not visited[x-1][y]:
                    visited[x-1][y]=True
                    myStack.append((x-1,y))
                if x+1<n and arr[x+1][y]=="1" and not visited[x+1][y]:
                    visited[x+1][y]=True
                    myStack.append((x+1,y))
                if y-1>=0 and arr[x][y-1]=="1" and not visited[x][y-1]:
                    visited[x][y-1]=True
                    myStack.append((x,y-1))
                if y+1<n and arr[x][y+1]=="1" and not visited[x][y+1]:
                    visited[x][y+1]=True
                    myStack.append((x,y+1))
            result.append(cnt)
print(len(result))
print("\n".join(str(element) for element in sorted(result)))