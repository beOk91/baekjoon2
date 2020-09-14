n,m=map(int,input().strip().split())
board,cnt=[[""]*m for _ in range(n)],0
for i in range(n):
    board[i]=list(input().strip())
    if i%2==0:cnt+=sum(1 if (j%2==0 and board[i][j]=="B") or (j%2!=0 and board[i][j]=="W") else 0 for j in range(m))
    else:cnt+=sum(1 if (j%2==0 and board[i][j]=="W") or (j%2!=0 and board[i][j]=="B") else 0 for j in range(m))
print(cnt)