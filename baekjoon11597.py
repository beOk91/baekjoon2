import sys
n=int(sys.stdin.readline().strip())
people=[0]*n
for i in range(n):
    people[i]=int(sys.stdin.readline().strip())
people.sort()
minval=2000000
for i in range(n//2):
    if people[i]+people[n-i-1]<minval:
        minval=people[i]+people[n-i-1]
print(minval)
