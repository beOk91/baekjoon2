l,r,a=map(int,input().strip().split())
l,r=r if l<r else l,l if l<r else r
print((r+a)*2 if l-r>a else ((l+a//2)*2 if l==r else (r+(a-(r-l))//2)*2))
  
if l-r>a:
    print((r+a)*2)
elif l==r:
    print((l+a//2)*2)
else:
    print("ㅎ2")
    print((r+a-(l-r))*2)

    
