a,b,c=map(int,input().strip().split())
d=int(input())
print((a*3600+b*60+c+24*60*60+d)//3600%24,(a*3600+b*60+c+24*60*60+d)//60%60,(a*3600+b*60+c+24*60*60+d)%60)