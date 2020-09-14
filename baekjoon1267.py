n=int(input())
n_list=list(map(int,input().strip().split()))
youngsik=[(i//30+1)*10 for i in n_list]
minsik=[(i//60+1)*15 for i in n_list]
print("M" if sum(minsik)<sum(youngsik) else "Y" if sum(youngsik)<sum(minsik) else "Y M", min(sum(youngsik),sum(minsik)) )