import math
n=int(input())
n_list=map(int,input().strip().split())
m=int(input())
m_list=map(int,input().strip().split())
A,B=1,1
for element in n_list:
    A*=element
for element in m_list:
    B*=element
AB_gcd=str(math.gcd(A,B))
print(AB_gcd[len(AB_gcd)-9:] if len(AB_gcd)>9 else AB_gcd)
