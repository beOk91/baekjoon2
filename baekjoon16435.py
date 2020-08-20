fruit_cnt,snakebird=map(int,input().strip().split())
fruit_list=list(map(int,input().strip().split()))
fruit_list.sort()
idx=0
while idx!=len(fruit_list):
    if snakebird>=fruit_list[idx]:
        snakebird+=1
        idx+=1
    else:
        break
print(snakebird)