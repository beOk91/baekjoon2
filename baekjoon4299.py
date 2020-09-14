a_plus_b,a_minus_b=map(int,input().strip().split())
if a_plus_b-a_minus_b<0 or (a_plus_b-a_minus_b)%2!=0:
    print(-1)
else:
    b=(a_plus_b-a_minus_b)//2
    a=a_plus_b-b
    print(max(b,a),min(a,b))