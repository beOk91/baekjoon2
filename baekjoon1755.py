num_play={
    "0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five",
    "6":"six","7":"seven","8":"eight","9":"nine","zero":"0",
    "one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7",
    "eight":"8","nine":"9"
}
m,n=map(int,input().strip().split())
arr=[" ".join (num_play[i] for i in str(element)) for element in range(m,n+1)]
arr.sort()
arr=["".join(num_play[e] for e in element.split()) for element in arr]
for i in range(1,len(arr)+1):
    print(arr[i-1],end=" ")
    if i!=0 and i%10==0:print()