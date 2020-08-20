text=list(map(int,input()))
text.sort(reverse=True)
print("".join(str(element) for element in text))