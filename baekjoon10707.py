x=int(input())
y_price=int(input())
y_limit=int(input())
y_price2=int(input())
joi_water_ant=int(input())
print(min(x*joi_water_ant,y_price if y_limit>=joi_water_ant else y_price+ (joi_water_ant-y_limit)*y_price2))