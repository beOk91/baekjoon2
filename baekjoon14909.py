n_list=list(map(int,input().strip().split()))
print(sum([1 if element>0 else 0 for element in n_list]))