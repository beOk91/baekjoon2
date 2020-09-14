cnt=0
for i in range(8):
    a=input().strip()
    cnt+=sum(1 if ((i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)) and a[j]=="F" else 0 for j in range(8))
print(cnt)