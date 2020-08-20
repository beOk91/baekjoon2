x=int(input())
num=1
while True:
    if num*(num+1)//2>=x:
        break
    else:
       num+=1
val=x-(num-1)*num//2-1
if num%2==0:
    print(str(1+val)+"/"+str(num-val))
else:
    print(str(num-val)+"/"+str(1+val))