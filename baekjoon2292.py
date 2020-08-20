import sys
n=int(sys.stdin.readline().strip())

i=1
while True:
    bee_house_cnt=1 if i==1 else 3*i*(i+1)-6*i 
    bee_house_cnt= bee_house_cnt+1 if i!=1 else bee_house_cnt
    if bee_house_cnt>=n:
        break
    else:
        i+=1
print(i)