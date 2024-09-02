#user input
m = input("masukkan nilai m (m > n): ")
m = int(m)
n = input("masukkan nilai n (m > n): ")
n = int(n)
#menghitung 
sisi1 = m ** 2 - n ** 2 
sisi2 = 2 * m * n 
sisimiring = m ** 2 + n ** 2
print("dengan m", m,"dan n", n, "maka memiliki sisi1", sisi1, ", sisi2", sisi2, ",dan sisi miring", sisimiring)