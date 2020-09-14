import sys
n=int(sys.stdin.readline().strip())
n_list=list(map(int,sys.stdin.readline().strip().split()))
arr={}
for element in n_list:
    arr[element]=1
m=int(input())
m_list=list(map(int,sys.stdin.readline().strip().split()))
for element in m_list:
    print(arr.get(element,0))