#membuat variabel di python
nama = "Andi"
umur = 25
tinggi = 170.5
is_active = True

print(nama)      # Andi
print(umur)      # 25
print(tinggi)    # 170.5
print(is_active) # True


#multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30

x = y = z = 100
print(x, y, z)  # 100 100 100


#mengecek tipe data variabel
nama = "Andi"
umur = 25
tinggi = 170.5

print(type(nama))   # <class 'str'>
print(type(umur))   # <class 'int'>
print(type(tinggi)) # <class 'float'>

#menghapus variabel
x = 10
print(x)  # 10

del x
# print(x)  # ❌ Error karena variable sudah dihapus
