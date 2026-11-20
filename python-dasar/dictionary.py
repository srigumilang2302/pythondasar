# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

# mengakses data dalam dictionary
print(mahasiswa["nama"])    # Budi
print(mahasiswa.get("umur")) # 20

# menambahkan data dan mengubah data dalam dictionary
mahasiswa["angkatan"] = 2023   # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)

# menghapus data dalam dictionary
mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)

# iterasi dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)

#nested dictionary
kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Budi
