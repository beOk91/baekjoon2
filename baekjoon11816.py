text=input()
print(int(text,16) if text[0:2]=="0x" else int(text,8) if text[0]=="0" else text )
