n=int(input())
student=[]
for _ in range(n):
    student.append(list(map(int,input().strip().split())))
student.sort(key=lambda x:x[2],reverse=True)
winner=[]
winner.append(student.pop(0))
winner.append(student.pop(0))
if winner[0][0] ==winner[1][0]:
    for element in student:
        if element[0]!=winner[0][0]:
            winner.append(element);break
else:winner.append(student.pop(0))
print("\n".join(str(e[0])+" "+str(e[1]) for e in winner))