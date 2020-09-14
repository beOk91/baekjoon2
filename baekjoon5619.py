import itertools,sys
n=int(sys.stdin.readline().strip())
n_list=[]
for _ in range(n):
    n_list.append(sys.stdin.readline().strip())
n_list.sort(key=lambda x:int(str(x)[0]))
print(n_list[2]+)
n_list=sorted([int(element[0]+element[1]) for element in list(itertools.permutations(n_list[:3],2))])
print(n_list[2])


1000
100
10000
9
8
7
6
5
4
3
2
1


9 10 11 19 50
"""
9 10 11 12
"""
910
911
919
950
109
1011
1019
1050
119
199
