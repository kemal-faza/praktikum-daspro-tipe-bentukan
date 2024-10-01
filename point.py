"""
Program   : Tipe Titik
Deskripsi : Menentukan tipe titik yang terdiri dari nilai absis (x) dan ordinat (y)
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 29/09/2024

**************************************************************
DEFINISI DAN SPESIFIKASI TYPE
type point : < x : real, y : real >
    <x, y> adalah sebuah titik atau point dengan x adalah absis dan y adalah ordinat

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

absis : point ---> integer
    absis(P) mengembalikan absis dari titik P
ordinat : point ---> integer
    ordinat(P) mengembalikan ordinat dari titik P

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakePoint : 2 integer ---> point
    MakePoint(x,y) membuat titik dengan absis x dan ordinat y

**************************************************************
DEFINISI DAN SPESIFIKASI OPERATOR

jarak : 2 point ---> integer
    jarak(P1,P2) menghitung jarak dari P1 ke P2
jarak0 : point ---> integer
    jarak0(P) menghitung jarak dari P ke (0,0)
kuadran : point ---> string
    kuadran(P) menentukan kuadran dari titik P
**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
fx2 : integer ---> integer
    fx2(x) mengembalikan nilai x kuadrat

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI PREDIKAT

IsOrigin : point ---> boolean
    IsOrigin(P) menentukan apakah titik P adalah titik (0,0)

**************************************************************

REALISASI
**************************************************************
"""

from math import sqrt


# Fungsi Antara
def fx2(x):
    return x * x


# Konstruktor
def MakePoint(x, y):
    return [x, y]


# Selektor
def absis(P):
    return P[0]


def ordinat(P):
    return P[1]


# Predikat
def IsOrigin(P):
    return (absis(P) == 0) and (ordinat(P) == 0)


# Operator
def jarak(P1, P2):
    return sqrt(fx2(absis(P1) - absis(P2)) + fx2(ordinat(P1) - ordinat(P2)))


def jarak0(P):
    return jarak(MakePoint(0, 0), P)


def kuadran(P):
    if absis(P) > 0 and ordinat(P) > 0:
        return f"Titik ({absis(P)}, {ordinat(P)}) berada di kuadran 1"
    elif absis(P) < 0 and ordinat(P) > 0:
        return f"Titik ({absis(P)}, {ordinat(P)}) berada di kuadran 2"
    elif absis(P) < 0 and ordinat(P) < 0:
        return f"Titik ({absis(P)}, {ordinat(P)}) berada di kuadran 3"
    elif absis(P) > 0 and ordinat(P) < 0:
        return f"Titik ({absis(P)}, {ordinat(P)}) berada di kuadran 4"


"""
APLIKASI
**************************************************************
"""

print(jarak(MakePoint(1, 1), MakePoint(4, 5)))
print(jarak0(MakePoint(3, 4)))
print(kuadran(MakePoint(2, -3)))
print(IsOrigin(MakePoint(1, 1)))
print(IsOrigin(MakePoint(0, 0)))
