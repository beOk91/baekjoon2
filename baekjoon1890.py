n=int(input())
board=[[0]*n for _ in range(n)]
for i in range(n):
    board[i]=list(map(int,input().strip().split()))
dp=[[-1]*n for _ in range(n)]
def f(y,x):
    if y==n-1 and x==n-1:return 1
    if y>n-1 or x>n-1:return 0
    if board[y][x]==0:return 0
    if dp[y][x]!=-1:return dp[y][x]
    ret=0
    ret+=f(y+board[y][x],x)
    ret+=f(y,x+board[y][x])
    dp[y][x]=ret
    return dp[y][x]
print(f(0,0))