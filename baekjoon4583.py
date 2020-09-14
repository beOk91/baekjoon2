while True:
    text=input()
    if text=="#":break
    text=text[::-1]
    result=""
    for i in range(len(text)):
        if text[i]=="d":result+="b"
        elif text[i]=="b":result+="d"
        elif text[i]=="p":result+="q"
        elif text[i]=="q":result+="p"
        elif text[i] in ["o","w","x","i","v"]:result+=text[i]
        else:result="INVALID";break
    print(result)