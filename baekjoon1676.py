n=int(input())
cnt=1
for i in range(1,n+1):
    cnt*=i
cnt=str(cnt)[::-1]
for i in range(len(cnt)):
    if cnt[i]!="0":
        print(i);break