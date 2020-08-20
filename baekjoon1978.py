num=int(input())
num_list=list(map(int,input().strip().split()))
for element in num_list:
    cnt=0
    if element==1:
        num-=1
    else:
        for j in range(element,0,-1):
            if cnt>2:
                num-=1
                break
            if element%j==0:
                cnt+=1
print(num)