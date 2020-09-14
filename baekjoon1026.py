n=int(input())
result=0
a_list=sorted(map(int,input().strip().split()))
b_list=list(map(int,input().strip().split()))
for _ in range(n):
    result+=(b_list.pop(b_list.index(max(b_list)))*a_list.pop(0))
print(result)
