n=int(input())
n_list=[]
for _ in range(n):
    n_list.append(input())
check=[True]*len(n_list[0])
for i in range(1,n):
    for j in range(0,len(n_list[0])):
        if n_list[i-1][j]!= n_list[i][j]:
            check[j]=False
print("".join(n_list[0][i] if check[i] else "?" for i in range(len(n_list[0]))))