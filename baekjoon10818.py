num=int(input())
num_list=input().split()
num_list2=[i for i in range(num)]
for i in range(num):
    num_list2[i]=int(num_list[i])
print(min(num_list2),max(num_list2))

"""
import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
print("%d %d" % (min(num_list),max(num_list)))

-------------------

n=int(input())
b=map(int, input().split() )
c=list(b)

print(min(c), max(c))
"""