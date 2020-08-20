import math
gcd_val,lcm_val=map(int,input().strip().split())

ab_2=lcm_val//gcd_val
idx=int(math.sqrt(ab_2))
while True:
    if ab_2%idx==0 and math.gcd(idx,ab_2//idx)==1:
        break
    idx-=1
print(idx*gcd_val,ab_2//idx*gcd_val)

"""
35 771260
->
980 27545
내답: 3955 6825
"""