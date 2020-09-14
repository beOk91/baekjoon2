n=list(map(int,input().strip().split()))
for i in range(1,len(n)):
    if n[i-1]>n[i]:print("Bad");break
    if i==len(n)-1 and n[i-1]<=n[i]:print("Good")
if 1==len(n):print("Good")