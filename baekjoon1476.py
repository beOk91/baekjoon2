import sys
e,s,m=map(int,sys.stdin.readline().strip().split())
arr1=[element for element in range(1,16)]
arr2=[element for element in range(1,29)]
arr3=[element for element in range(1,20)]
n=0
while True:
    if arr2[(15*n+e)%28-1]==s and arr3[(15*n+e)%19-1]==m:break
    n+=1
print(15*n+e)