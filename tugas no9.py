#user input
pH = input("panjang halaman: ")
pH = int(pH)
lH = input("lebar halaman: ")
lH = int(lH)
pR = input("panjang rumah: ")
pR = int(pR)
lR = input("lebar rumah: ")
lR = int(lR)
#hitung luas halaman dan rumah
LH = pH * lH
LR = pR * lR 
#area yang dipotong 
area = LH - LR 
#kecepatan pemotongan
kec = 2 
#hitung waktu memotong
waktu = area / kec 
print("dibutuhkan", waktu,"detik untuk memotong", area, "kaki persegi")
 