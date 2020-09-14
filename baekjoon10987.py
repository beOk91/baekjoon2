text=input()
print(sum(1 if element in ["a","e","i","o","u"] else 0 for element in text))