import sys
n=int(sys.stdin.readline())
arr=[[9.23076, 26.7, 1.835],[1.84523,75,1.348],
[56.0211,1.5,1.05],[4.99087,42.5,1.81],
[0.188807,210, 1.41],[15.9803,3.8,1.04],
[0.11193,254,1.88]]
for _ in range(n):
    total=list(map(int,sys.stdin.readline().split()))
    result=0
    for i in range(len(total)):
        if i%3==0:result+=int(arr[i][0]*((arr[i][1]-total[i])**arr[i][2]))
        else:result+=int(arr[i][0]*((total[i]-arr[i][1])**arr[i][2]))
    print(result)