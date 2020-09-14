import sys
x,y,w,s=map(int,sys.stdin.readline().strip().split())
print(min((x+y)*w,(min(x,y)*s+(max(x,y)-min(x,y))*w) ))