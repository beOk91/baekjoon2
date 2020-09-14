n=int(input().strip())
seriel_num=[]
for _ in range(n):
    seriel_num.append(input().strip())
seriel_num.sort()
seriel_num.sort(key=lambda x:(len(x),sum(int(e) for e in x if e.isnumeric())))
print("\n".join(element for element in seriel_num))