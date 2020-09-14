import sys
n=int(sys.stdin.readline().strip())
n_list=list(map(int,sys.stdin.readline().strip().split()))
my_dictionary={}
for e in n_list:
    my_dictionary[e]=my_dictionary.get(e,0)+1
m=int(sys.stdin.readline().strip())
m_list=list(map(int,sys.stdin.readline().strip().split()))
for e in m_list:
    print(my_dictionary.get(e,0),end=" ")