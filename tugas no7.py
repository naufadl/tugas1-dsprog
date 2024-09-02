#user input
gallons = input("ada berapa galon: ")
gallons = float(gallons)
#informasi
g = 42
BTU1 = 5800000
efficiency = 0.65
#menghitung BTU yang disalurkan
BTUdit = (gallons * BTU1 / g) * efficiency
BTUdit = round(BTUdit,0)
print("BTU yang disalurkan untuk", gallons, "galon adalah", BTUdit, "BTU")