num=int(input())
num_list=list(map(int,input().strip().split()))
sosu=[False]*1001
for element in num_list:
    sosu[element]=True
sosu[1]=False
for i in range(2,1001):
    for j in range(i+i,1001,i):
        sosu[j]=False

print(sum(1 if sosu[i] else 0 for i in range(1001)))