def conversion(n1,n2):
    if n1<n2:
        return str(n1)
    else:
        return conversion(n1//n2,n2)+str(n1%n2)
while True:
    cmd=input().strip()
    if cmd[0]=="0":break
    b,p,m=cmd.split()
    print(conversion(int(p,int(b))%int(m,int(b)),int(b)))