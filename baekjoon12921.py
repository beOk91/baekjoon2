def solution(n):
    result=set(i for i in range(2,n+1))
    for i in range(2,n+1):
        result-=set(i for i in range(2*i,n+1,i))
    return len(result)