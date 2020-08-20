n_list=list(map(int,input().strip().split()))
result=0
for element in n_list:
    result+=(element**2)
print(result%10)