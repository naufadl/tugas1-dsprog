print("TAXI FARE CALCULATOR")
#input user
awal = input("Enter beginning odometer reading")
awal = float(awal)
akhir = input("Enter ending odometer reading")
akhir = float(akhir)
#menghitung jarak
selisih = akhir - awal 
selisih = round(selisih,2)
#menghitung harga
harga = selisih * 1.5
harga = round(harga,2)
print("you traveled a distance of", selisih, "miles. at $1.50 per mile, your fare is", harga )