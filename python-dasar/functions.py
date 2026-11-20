#function def
def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()

#function dengan parameter
def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Siti")

#function dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)

#default parameter
def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Andi")  # Menggunakan parameter
sapa_orang()        # Menggunakan default

#function dengan banyak argument (*args dan **kwargs)
# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  # Bisa input banyak angka


# **kwargs
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")