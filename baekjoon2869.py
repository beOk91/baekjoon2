a,b,v=map(int,input().strip().split())
day= v//(a-b)
print(day-2 if a-b<b else day-1)