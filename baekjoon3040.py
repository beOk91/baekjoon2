dwarf=[]
for _ in range(9):
    dwarf.append(int(input()))
for i in range(9):
    for j in range(i+1,9):
        if dwarf[i]+dwarf[j]==(sum(dwarf)-100):
            dwarf.pop(j)
            dwarf.pop(i)
            break
    if sum(dwarf)==100:
        break
print("\n".join(str(element) for element in dwarf))
