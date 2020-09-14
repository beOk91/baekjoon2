a_b,a_c,b_c=map(int,input().strip().split())
b=(a_b-a_c+b_c)/2
a=a_b-b
c=a_c-a
print(str(-1) if a<1 or b<1 or c<1 else 1)
if a>=1 and b>=1 and c>=1:print(a,b,c)