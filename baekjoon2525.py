a,b=map(int,input().strip().split())
c=int(input())
print((a*60+b+c+24*60)//60%24,(a*60+b+c)%60)