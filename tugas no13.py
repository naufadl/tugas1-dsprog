#input user
Jsiswa = input("jumlah siswa yang terdaftar: ")
Jsiswa = int(Jsiswa)
#kapasitas per grup
K = 30
#menghitung
Jgrup = Jsiswa / K
Jgrup = round(Jgrup,0)
Ssisa = Jsiswa % K 
print(f"jumlah grup yang terbentuk dari {Jsiswa} siswa dengan kapasitas per grup {K} siswa adalah {Jgrup} dan sisa {Ssisa} siswa")