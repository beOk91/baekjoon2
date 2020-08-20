cnt=1
while True:
    num=int(input())
    if num==0:
        break
    else:
        num*=3
        num1=num
        num=num//2 if num%2==0 else (num+1)//2
        num=num*3//9
        print("{}.".format(cnt)+(" odd" if num1%2!=0 else " even")+" {}".format(num))
        cnt+=1