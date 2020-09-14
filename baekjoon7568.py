n=int(input().strip())
people=[]
for _ in range(n):
    people.append(list(map(int,input().strip().split())))
print(" ".join(str(sum(1 if people[i][0]<people[j][0] and people[i][1]<people[j][1] else 0 for j in range(n))+1) for i in range(n)))