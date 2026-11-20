from my_package import operasi, geometri

print(operasi.kurang(10, 4))          # 6
print(geometri.luas_persegi(5))       # 25

from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))                  # 13
print(luas_persegi(8))                # 64