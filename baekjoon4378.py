arr=["`","1","2","3","4","5","6","7","8","9","0","-","=","Q","W","E","R","T","Y","U","I","O","P","[","]","\\","A","S","D","F","G","H","J","K","L",";","'","Z","X","C","V","B","N","M",",",".","/"]
while True:
    try:
        text=input().strip().split()
        print(" ".join("".join(arr[arr.index(j)-1] for j in element) for element in text))
    except:
        break