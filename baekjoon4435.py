n=int(input())
gandalf_score=[1,2,3,3,4,10]
sauron_score=[1,2,2,2,3,5,10]
for i in range(1,n+1):
    gandalf=list(map(int,input().strip().split()))
    gandalf_sum=sum(gandalf_score[i]*gandalf[i] for i in range(6))
    sauron=list(map(int,input().strip().split()))
    sauron_sum=sum(sauron_score[i]*sauron[i] for i in range(7))
    print("Battle {}: ".format(i)+("Evil eradicates all trace of Good" if gandalf_sum<sauron_sum else "Good triumphs over Evil" if gandalf_sum>sauron_sum else "No victor on this battle field"))