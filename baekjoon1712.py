a,b,c=map(int,input().strip().split())
cnt=-1
if c>b:
    cnt=a//(c-b)+1
print(cnt)