# Membagi angka dengan nol
#angka = 10
#hasil = angka / 0
#print("Hasil:", hasil)

# Menangani exception dengan try-except
try:
    angka = 10
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")

# menangani banyak jenis error
try:
    data = int("abc")   # error konversi string ke int
except ValueError:
    print("Error: Data tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak boleh membagi dengan nol!")

# menggunakan else dan finally
try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)
finally:
    print("Selesai memproses.")

# membuat exception sendiri
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)

try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)