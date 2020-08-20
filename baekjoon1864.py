try:
    arr={"-":0,"\\":1,"(":2,"@":3,"?":4,">":5,"&":6,"%":7,"/":-1}
    while True:
        text=input()
        result=0
        for i in range(len(text)):
            result+=arr[text[i]]*(8**(len(text)-1-i))
        print(result)
except:
    exit()