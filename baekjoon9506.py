while True:
    n=int(input())
    if n==-1:break
    arr=[1]+[i for i in range(2,n//2+1) if n%i==0]
    print(str(n)+" = "+ " + ".join(str(i) for i in arr) if sum(arr)==n else str(n)+ " is NOT perfect.")