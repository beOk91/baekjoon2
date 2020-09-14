x1,y1,x2,y2=map(int,input().strip().split())
x3,y3,x4,y4=map(int,input().strip().split())

print(abs(max(x1,x2)-max(x3,x4))*abs(max(y1,y2)-max(y3,y4)))