n=int(input())
text=input()
print(sum([1 for element in text if element in ["a","e","i","o","u"]]))