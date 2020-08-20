import math
def m_lcm(arr):
    arr2=arr
    if len(arr2)==1:
        return arr2[0]
    elif len(arr2)>2:
        a=arr2.pop()
        b=arr2.pop()
        arr2.append(a*b//math.gcd(a,b))
        return m_lcm(arr2)
    else:
        a=arr2.pop()
        b=arr2.pop()
        return a*b//math.gcd(a,b)

n=input()
n_list=list(map(int,input().strip().split()))
print(m_lcm(n_list))
