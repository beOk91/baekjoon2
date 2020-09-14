import sys
n,m=map(int,sys.stdin.readline().strip().split())
n_score=list(map(int,sys.stdin.readline().strip().split()))
students=[]
for _ in range(m):
    student=sys.stdin.readline().strip().split()
    score=0
    for i in range(n):
        if student[i+1]=="O":score+=n_score[i]
    students.append((int(student[0]),score))
students.sort(key=lambda x:(-x[1],x[0]))
print(students[0][0],students[0][1])