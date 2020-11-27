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
