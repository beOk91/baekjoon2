import sys
n=int(sys.stdin.readline().strip())

for i in range(n//5,-1,-1):
    if ((n-i*5)%3)==0:
        print(i+((n-i*5)//3))
        break
    elif i==0 and n%3!=0:
        print(-1)