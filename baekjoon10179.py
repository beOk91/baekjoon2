n=int(input())
print("\n".join(str("$%.2f" %(round(float(input())*0.8,2))) for _ in range(n)))