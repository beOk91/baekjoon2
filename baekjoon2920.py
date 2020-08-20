n_list=list(map(int,input().strip().split()))
flag=""
for i in range(7):
    if n_list[i]<=n_list[i+1]:
        if flag=="descending":
            flag="mixed"
            break
        else:
            flag="ascending"
    elif n_list[i]>=n_list[i+1]:
        if flag=="ascending":
            flag="mixed"
            break
        else:
            flag="descending"
print(flag)