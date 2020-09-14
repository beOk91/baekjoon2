n,m=map(int,input().strip().split())
q_list=[element for element in range(1,n+1)]
for _ in range(m):
    a,b=map(int,input().strip().split())
    q_list.insert(q_list.index(b),q_list.pop(q_list.index(a)))
print(" ".join(str(element) for element in q_list))
    