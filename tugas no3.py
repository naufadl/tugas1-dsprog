print("menghitung suhu")
jam = input("jam: ")
jam = int(jam)
menit = input("menit: ")
menit = int(menit)
menit = menit / 60
menit = float(menit) 
t = jam + menit 
T = 4 * t ** 2 / ( t + 2 ) - 20
T = round(T,1)
print("jadi suhunya adalah", T, "celcius")