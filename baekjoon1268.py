import sys
n=int(sys.stdin.readline().strip())
board=[[0]*5 for _ in range(n)]
for i in range(n):
    grade=list(map(int,sys.stdin.readline().strip().split()))
    board[i]=grade
leader=[]
for j in range(n):
    total=0
    for i in range(5):
        total+=([board[e][i] for e in range(n)].count(board[j][i])-1)
    leader.append(total)
print(leader.index(max(leader))+1)