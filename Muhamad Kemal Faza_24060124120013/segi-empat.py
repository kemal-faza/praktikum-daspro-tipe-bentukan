"""
Program   : Tipe Segiempat
Deskripsi : Menentukan tipe segiempat yang terdiri dari empat buah baris
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 29/09/2024

**************************************************************
DEFINISI DAN SPESIFIKASI TYPE
type segiempat : < g1 : garis, g2 : garis, g3 : garis, g4 : garis >
    <g1, g2, g3, g4> adalah sebuah segiempat yang terdiri dari empat buah baris yaitu g1, g2, g3, g4

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

garis1 : segiempat ---> garis
    garis1(r) mengembalikan garis pertama dari segiempat r
garis2 : segiempat ---> garis
    garis2(r) mengembalikan garis kedua dari segiempat r
garis3 : segiempat ---> garis
    garis3(r) mengembalikan garis ketiga dari segiempat r
garis4 : segiempat ---> garis
    garis4(r) mengembalikan garis keempat dari segiempat r

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakeSegiempat : 4 garis ---> segiempat
    MakeSegiempat(g1, g2, g3, g4) membuat segiempat dengan empat buah garis g1, g2, g3, dan g4

**************************************************************
DEFINISI DAN SPESIFIKASI OPERATOR

AreaBujurSangkar : segiempat ---> real
    AreaBujurSangkar(r) menghitung luas bujur sangkar dari segiempat r

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI PREDIKAT

IsJajargenjang : segiempat ---> boolean
    IsJajargenjang(r) memerika apakah segiempat r adalah jajargenjang
IsBujurSangkar : segiempat ---> boolean
    IsBujurSangkar(r) memerika apakah segiempat r adalah bujur sangkar

**************************************************************

REALISASI
**************************************************************
"""

from math import sqrt


def fx2(x):
    return x * x


def absis(P):
    return P[0]


def ordinat(P):
    return P[1]


def jarak(P1, P2):
    return sqrt(fx2(absis(P1) - absis(P2)) + fx2(ordinat(P1) - ordinat(P2)))


def MakePoint(x, y):
    return [x, y]


def MakeGaris(p1, p2):
    return [p1, p2]


def PanjangGaris(g):
    return jarak(g[0], g[1])


# Fungsi Utama


# Konstruktor
def MakeSegiempat(g1, g2, g3, g4):
    return [g1, g2, g3, g4]


# Selektor
def garis1(g):
    return g[0]


def garis2(g):
    return g[1]


def garis3(g):
    return g[2]


def garis4(g):
    return g[3]


# Predikat
def IsBujurSangkar(r):
    return (
        PanjangGaris(garis1(r)) == PanjangGaris(garis2(r))
        and PanjangGaris(garis1(r)) == PanjangGaris(garis3(r))
        and PanjangGaris(garis1(r)) == PanjangGaris(garis4(r))
    )


def IsJajargenjang(r):
    return (
        PanjangGaris(garis1(r)) == PanjangGaris(garis3(r))
        and PanjangGaris(garis2(r)) == PanjangGaris(garis4(r))
        and PanjangGaris(garis1(r)) != PanjangGaris(garis2(r))
    )


# Operator
def AreaBujurSangkar(r):
    return PanjangGaris(garis1(r)) * PanjangGaris(garis2(r))


"""
APLIKASI
**************************************************************
"""
print(
    IsBujurSangkar(
        MakeSegiempat(
            MakeGaris(
                MakePoint(0, 0),
                MakePoint(5, 0),
            ),
            MakeGaris(
                MakePoint(5, 0),
                MakePoint(5, 5),
            ),
            MakeGaris(
                MakePoint(5, 5),
                MakePoint(0, 5),
            ),
            MakeGaris(
                MakePoint(0, 5),
                MakePoint(0, 0),
            ),
        )
    )
)

print(
    IsJajargenjang(
        MakeSegiempat(
            MakeGaris(
                MakePoint(-1, 0),
                MakePoint(5, 0),
            ),
            MakeGaris(
                MakePoint(5, 0),
                MakePoint(6, 5),
            ),
            MakeGaris(
                MakePoint(6, 5),
                MakePoint(0, 5),
            ),
            MakeGaris(
                MakePoint(0, 5),
                MakePoint(-1, 0),
            ),
        )
    )
)

print(
    AreaBujurSangkar(
        MakeSegiempat(
            MakeGaris(
                MakePoint(0, 0),
                MakePoint(5, 0),
            ),
            MakeGaris(
                MakePoint(5, 0),
                MakePoint(5, 5),
            ),
            MakeGaris(
                MakePoint(5, 5),
                MakePoint(0, 5),
            ),
            MakeGaris(
                MakePoint(0, 5),
                MakePoint(0, 0),
            ),
        )
    )
)
