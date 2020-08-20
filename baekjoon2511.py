a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
score=[0]*2
for i in range(10):
    if a[i]>b[i]:
        score[0]+=3
    elif a[i]<b[i]:
        score[1]+=3
    else:
        score[0]+=1
        score[1]+=1
print(score[0],score[1])
winner="A" if score[0]>score[1] else "B" if score[0]<score[1] else ""
if score[0]==score[1] and score[1]==10:
    winner="D"
elif score[0]==score[1]:
    for i in range(9,-1,-1):
        if a[i]>b[i]:
            winner="A"
            break
        elif a[i]<b[i]:
            winner="B"
            break
        else:
            continue
print(winner)