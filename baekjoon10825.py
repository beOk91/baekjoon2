n=int(input())
score=[]
for _ in range(n):
    student=input().strip().split()
    score.append((student[0],int(student[1]),int(student[2]),int(student[3])))
score.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
print("\n".join(element[0] for element in score))