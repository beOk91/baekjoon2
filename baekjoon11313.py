import sys
n=int(sys.stdin.readline().strip())
n_people=[]
for _ in range(n):
    n_people=n_people+[sys.stdin.readline().strip()]
n_people.sort(key=lambda x: (x.split()[1],x.split()[0]))

q=int(sys.stdin.readline().strip())
for _ in range(q):
    person=sys.stdin.readline().strip()
    idx=n_people.index(person)
    if idx%3==0:print(n_people[idx+1]+"\n"+n_people[idx+2])
    elif idx%3==1:print(n_people[idx-1]+"\n"+n_people[idx+1])
    else:print(n_people[idx-2]+"\n"+n_people[idx-1])
    