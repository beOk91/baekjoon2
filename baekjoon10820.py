try:
    while True:
        text=input()
        arr=[0]*4
        for element in text:
            if element >='A' and element<='Z':arr[1]+=1
            elif element >='a' and element<='z':arr[0]+=1
            elif element>='0' and element<='9':arr[2]+=1
            elif element==" ":arr[3]+=1
        print(" ".join(str(element) for element in arr))
except:
    exit()