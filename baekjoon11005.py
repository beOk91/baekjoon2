def f(num,num2):
    arr="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num<num2:return arr[num]
    else:return f(num//num2,num2)+arr[num%num2]
n,b=map(int,input().strip().split())
print(f(n,b))