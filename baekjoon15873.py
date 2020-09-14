text=input()
a,b=int(text[0]) if len(text)==2 else 10 if text[1]=="0" else int(text[0]) ,int(text[1]) if len(text)==2 else 10 if text[-1]=="0" else int(text[-1])
print(a+b)