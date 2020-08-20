n=int(input())
n_list=list(map(int,input().strip().split()))
arr={}
for element in n_list:

for element in n_list:
    arr[element]+=1
m=int(input())
m_list=list(map(int,input().strip().split()))

for element in m_list:
    if arr[element]>0:
        print("1")
    else:
        print("0")