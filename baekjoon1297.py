c,w_r,h_r=map(int,input().strip().split())
r=c/((w_r**2+h_r**2)**0.5)
print(int(w_r*r),int(h_r*r))