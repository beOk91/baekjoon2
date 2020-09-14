text=input().strip()
text="0"*(3-len(text)%3 if len(text)%3!=0 else 0)+text
arr={"000":0,"001":1,"010":2,"011":3,"100":4,"101":5,"110":6,"111":7}
print("".join(str(arr.get(text[i:i+3])) for i in range(0,len(text),3)))