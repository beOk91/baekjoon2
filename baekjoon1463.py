import sys
x=int(sys.stdin.readline().strip())
x_road=[0]*1000001
for i in range(x,0,-1):
    if i%3==0:
        x_road[i//3]=min(x_road[i//3],x_road[i]+1) if x_road[i//3]!=0 else x_road[i]+1
    elif i%2==0:
        x_road[i//2]=min(x_road[i//2],x_road[i]+1) if x_road[i//2]!=0 else x_road[i]+1
    x_road[i-1]=min(x_road[i-1],x_road[i]+1) if x_road[i-1]!=0 else x_road[i]+1
print(x_road[1])
