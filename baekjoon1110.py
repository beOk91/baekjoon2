def f(num):
    newNum,cnt=num%10*10+(num//10+num%10)%10,1
    while newNum!=num:
        newNum=newNum%10*10+(newNum//10+newNum%10)%10
        cnt+=1
    return cnt
        
num=int(input())
print(f(num))