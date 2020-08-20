while True:
    text=input()
    if text==".":
        break
    else:
        for i in range(1,len(text)+1):
            if len(text)%i==0:
                start,end=0,i
                myNum=text[start:i]
                if text==myNum*(len(text)//len(myNum)):
                    print(len(text)//len(myNum))
                    break
        #print(myNum*(len(text)//len(myNum)))
        """
        while True:
            if text[start+i:end+i]==myNum:
                start+=i
                end+=i
            else:
                break
            if (end-1)==len(text) and text[start:end]==myNum:
                break
        if end==len(text) and text[start:end]==myNum:
            print(len(text)//len(myNum))
            break
        """