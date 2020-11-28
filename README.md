# Tugas Pertemuan 10 Bahasa Pemrograman - Lab 6 *(repo: p10_lab6)*

<hr>


Pada mata kuliah Bahasa Pemrograman Pertemuan 10, saya diberi materi oleh dosen yaitu. Fungsi, Module dan Package.<br>

## Latihan

Pada pembahasan kali ini saya diberikan tugas oleh dosen untuk mengerjakan sebuah program sederhana dalam sebuah Tugas Latihan.

* Dosen memberikan tugas seperti berikut :<br>
![Soal Latihan Lab 6](pict/soal-latihan.PNG) <br>

* Setelah saya membaca dan memahami materi yang diberikan oleh Dosen, dan mencari referensi dari Internet, entah itu dari Forum Programmer ataupun Modul-modul yang dishare oleh seseorang<br>

* Seperti berikut source code yang telah saya kerjakan untuk Tugas Latihan :<br>
``` python
import math

print("====================================")
print("Nama : FEBRO HERDYANTO")
print("NIM : 312010043")
print("Kelas : TI.20.B.1")
print("Mata Kuliah : Bahasa Pemrograman")
print("====================================")


def a(x):
    return x ** 2


def a2(x): x ** 2


print("1. Mengubah function menggunakan Lambda \n   def a(x): \n \t   return x ** 2")
print("   Hasil : def a2(x): x ** 2")


def b(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def b2(x, y): math.sqrt(x ** 2 + y ** 2)


print("-----------------------------------------")
print("2. Mengubah function menggunakan Lambda \n   def b(x, y): \n \t   return math.sqrt(x ** 2 + y ** 2)")
print("   Hasil : def b2(x, y): math.sqrt(x ** 2 + y ** 2)")


def c(*args):
    return sum(args) / len(args)


def c2(*args): sum(args) / len(args)


print("-----------------------------------------")
print("3. Mengubah function menggunakan Lambda \n   def c(*args): \n \t   return sum(args) / len(args)")
print("   Hasil : def c2(*args): sum(args) / len(args)")


def d(s):
    return "".join(set(s))


def d2(s): "".join(set(s))


print("-----------------------------------------")
print("4. Mengubah function menggunakan Lambda \n   def d(s): \n \t   return "".join(set(s))")
print("   Hasil : def d2(s): "".join(set(s))")
```

* Dari hasil source code diatas sebagai berikut :<br>
![Hasil Soal Latihan](pict/hasil-latihan.PNG)

* Dalam Tugas Latihan diatas saya menggunakan bahasa Lambda

<hr>

## Praktikum

Selain tugas latihan yang diberikan oleh dosen, saya juga diberi tugas praktikum oleh Dosen. Yaitu membuat progam sederhana menggunakan fungsi. Yang menampilkan Data Mahasiswa. <br>

* Seperti berikut tugas yang diberikan oleh dosen :<br>
![Tugas Praktikum Lab 6](pict/soal-praktikum.PNG)<br>

* a