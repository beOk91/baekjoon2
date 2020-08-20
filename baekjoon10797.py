n=input()
n_list=list(input().strip().split())
cnt=0
for element in n_list:
    if element[len(element)-1]==n:
        cnt+=1
print(cnt)