n=int(input())
n_list=list(map(int,input().strip().split()))
score=[0]*n
score[0]=n_list[0]
for i in range(1,n):
    if n_list[i-1]==1 and n_list[i]==1:
        score[i]=score[i-1]+1
    else:
        score[i]=n_list[i]
print(sum(score))