a=list(map(int,input().strip().split(":")))
b=list(map(int,input().strip().split(":")))
print((b[0]*60*60-a[0]*60*60+b[1]*60-60*a[1]+b[2]-a[2]+24*60*60)%86400)