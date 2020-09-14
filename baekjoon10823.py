text=""
try:
    while True:
        text+=input().strip()
except:
    print(sum(list(map(int,text.split(",")))))
    exit()