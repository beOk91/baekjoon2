def f(num):
    arr=["7","4"]
    if num==0:return ""
    if num==1:return "4"
    return (f(num//2-1) if num%2==0 else f(num//2)) + arr[num%2]
k=int(input())
print(f(k))