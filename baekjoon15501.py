import sys
n=int(sys.stdin.readline().strip())
arr1=list(map(int,sys.stdin.readline().strip().split()))
arr2=list(map(int,sys.stdin.readline().strip().split()))
chk=False
for i in range(n):
    val=arr1[n-i:]+arr1[0:(n-i)]
    if val==arr2 or val[::-1]==arr2:
        chk=True;break
print("good puzzle" if chk else "bad puzzle")