import sys
n=int(sys.stdin.readline().strip())
finger=[1,2,3,4,5,4,3,2]
print(finger[(n+7)%8])
