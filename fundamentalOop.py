from geometri import bangun_ruang
from geometri.bangun_ruang import BangunRuang
from geometri.persegi import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP Encapsulation')
print('\nMenghitung Luas Persegi')
p1 = PersegiPanjang(10,3)
print(p1.info())
print(p1.hitungLuas())

print('\nMenghitung Luas Segitiga')
s1 = Segitiga(20,6)
print(s1.info())
print(s1.hitungLuas())

print('\nMenggunakan OOP Inheritance')
b1 = BangunRuang()
print(b1.info())
print(b1.hitungLuas())

#polymorphism : kemampuang object untuk merespon berbeda , terhadap pemanggilan method yang sama
daftar_bangunRuang =[]
daftar_bangunRuang.append(p1)
daftar_bangunRuang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangunRuang:
    print(bangun_ruang.info())