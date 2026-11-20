# contoh program lengkap
# Menuulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())
