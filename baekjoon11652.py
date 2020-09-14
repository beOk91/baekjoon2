import sys
n=int(sys.stdin.readline().strip())
my_list={}
my_list2=[]
for _ in range(n):
    num=int(sys.stdin.readline().strip())
    my_list[num]=my_list.get(num,0)+1
    my_list2.append(num)
maxCnt=max(my_list.values())
for element in set(sorted(my_list2)):
    if my_list[element]==maxCnt:
        print(element);break
