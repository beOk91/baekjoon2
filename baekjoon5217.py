n=int(input())
for _ in range(n):
    num=int(input())
    print("Pairs for "+str(num)+": "+", ".join(str(i)+" "+str(j) for (i,j) in zip(range(1,num),range(num-1,0,-1)) if i<j))