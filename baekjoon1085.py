x,y,w,h=map(int,input().strip().split())
print(min(min(y,h-y),min(w-x,x)))