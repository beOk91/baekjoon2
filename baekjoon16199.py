birthday=list(map(int,input().strip().split()))
today=list(map(int,input().strip().split()))

if today[0]==birthday[0]:
    print(0)
elif birthday[1] < today[1] or (birthday[1] == today[1] and birthday[2]<= today[2]):
    print(today[0]-birthday[0])
else:
    print(today[0]-birthday[0]-1)
print(today[0]+1-birthday[0])
print(today[0]-birthday[0])