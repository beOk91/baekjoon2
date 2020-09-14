n=int(input())
start_num,cnt=666,0
while True:
    if "666" in str(start_num):
        cnt+=1
    if cnt==n:break
    start_num+=1
print(start_num)