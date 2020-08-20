dwarf=[]
for _ in range(9):
    dwarf.append(int(input()))
isNotDwarf=sum(dwarf)-100
for i in range(9):
    for j in range(i+1,9):
        if dwarf[i]+dwarf[j]==isNotDwarf:
            dwarf.pop(j)
            dwarf.pop(i)
            break
    if len(dwarf)==7:
        break
dwarf.sort()
print("\n".join(str(element) for element in dwarf))