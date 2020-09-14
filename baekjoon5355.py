t=int(input())
for _ in range(t):
    text=input().strip().split()
    result=float(text[0])
    for element in text[1:]:
        result= result*3 if element=="@" else result+5 if element=="%" else result-7 if element=="#" else result
    print("%.2f" %result)
            