k=int(input().strip())
for i in range(1,k+1):
    n_list=list(map(int,input().strip().split()))
    n_list2=sorted(n_list[1:],reverse=True)
    print("Class {}".format(i)+"\n"+"Max {}, Min {}, Largest gap {}".format(max(n_list2),min(n_list2),max(n_list2[i]-n_list2[i+1] for i in range(n_list[0]-1))))