n=int(input())
arr=[True]*((2**31)-1)
n_list=list(map(int,input().strip().split()))
for element in n_list:
    arr[element-1]=False
for i in range(len(arr)):
    if arr[i]==True:
        print(i+1);break