m=int(input())
n=int(input())
m_sqrt=int(m**(1/2))+1 if m**(1/2)%1!=0 else int(m**(1/2))
n_sqrt=int(n**(1/2))
sum1=0
if m_sqrt>n_sqrt:
    print(-1)
else:
    for i in range(m_sqrt,n_sqrt+1):
        sum1+=i*i
    print(sum1)
    print(m_sqrt*m_sqrt)