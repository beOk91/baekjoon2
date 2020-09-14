text=input()
for element in text:
    if element.islower():print(chr((ord(element)-97+26-13)%26+97),end="")
    elif element.isupper():print(chr((ord(element)-65+26-13)%26+65),end="")
    else:print(element,end="")