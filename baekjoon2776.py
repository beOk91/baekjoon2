t=int(input())
for _ in range(t):
    n=int(input())
    n_list=list(map(int,input().strip().split()))
    m=int(input())
    m_list=list(map(int,input().strip().split()))
    for element in m_list:
        print(1 if element in n_list else 0)