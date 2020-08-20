text=input()
text1=""
for element in text:
    if element >='a' and element<='z':
        text1+=element.upper()
    else:
        text1+=element.lower()
print(text1)