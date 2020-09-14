t=int(input().strip())
for i in range(1,t+1):
    n=int(input())
    n_list=list(map(int,input().strip().split()))
    sale_price=[]
    while len(sale_price)!=n:
        original=n_list.pop()
        sale_price=[n_list.pop(n_list.index(original*3/4))]+sale_price
    print("Case #"+str(i)+": "+" ".join(str(e) for e in sale_price))