def f(num):
    if num<2:
        return "1"+str(num)
    return f(num//2)+str(num%2)
n=int(input())
print(f(n))