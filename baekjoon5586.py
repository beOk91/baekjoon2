text=input()
print(sum(1 for i in range(len(text)-2) if text[i:i+3]=="JOI" ))
print(sum(1 for i in range(len(text)-2) if text[i:i+3]=="IOI" ))