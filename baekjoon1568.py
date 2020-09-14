import sys
n=int(sys.stdin.readline().strip())
time,flying_bird=0,0
while True:
    if n<=0:break
    time+=1
    flying_bird+=1
    if n<flying_bird:flying_bird=1
    n-=flying_bird
print(time)
