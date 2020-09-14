def f(n,a):
    if n<a:return str(n)
    return f(n//a,a)+str(n%a)
n=int(input().strip())
cnt=0
for i in range(2,11):
    newVal=f(n,i)
    print(newVal)
    #if newVal==newVal[::-1]:print(i,newVal);cnt+=1
if cnt==0:print("NIE")