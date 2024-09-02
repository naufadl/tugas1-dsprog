print("volume dan kecepatan")
VTBI = input("volume to be infused (ml)")
VTBI = int(VTBI)
menit = input("minutes over which to infuse")
menit = int(menit)
jam = menit / 60
jam = float(jam)
rate = VTBI / jam 
rate = float(rate)
print("VBTI", VTBI, "ml")
print("Rate", rate, "ml/hr")
