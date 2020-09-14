def f(num,num2):
    if num<num2:return [num]
    else:return f(num//num2,num2)+[num%num2]

a,b=map(int,input().strip().split())
m=int(input().strip())
a_list=list(map(int,input().strip().split()))[::-1]
original_num=0
for i in range(m):
    num=1
    for j in range(i):
        num*=a
    original_num+=num*a_list[i]
print(" ".join(str(e) for e in f(original_num,b)))