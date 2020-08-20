n=int(input())
score=list(map(int,input().strip().split()))
newScore=0
for element in score:
    newScore+=element/max(score)*100
print(newScore/n)