water = []
top = []

for i in range(3):
    water_price = int(input())
    if water_price >=100 and water_price <=500:
        water.append(water_price)
    else:
        water.append(0)


for i in range(2):
    top_price = int(input())
    if top_price >= 20 and top_price <= 80:
        top.append(top_price)
    else:
        top.append(0)


water_asc = sorted(water , reverse = False)
top_asc = sorted(top , reverse = False)
print(water_asc[0]+top_asc[0]+10)
