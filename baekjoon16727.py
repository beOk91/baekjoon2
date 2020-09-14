p1,e2=map(int,input().strip().split())
e1,p2=list(map(int,input().strip().split()))
print("Persepolis" if p1+p2>e1+e2 else "Esteghlal" if e1+e2>p1+p2 else "Persepolis" if p2>e2 else "Esteghlal" if e2>p2 else "Penalty")
