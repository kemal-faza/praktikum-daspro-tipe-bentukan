"""
Program   : Tipe Garis
Deskripsi : Menentukan tipe garis yang terdiri dari dua titik yaitu titik awal dan titik akhir
NIM/Nama  : 24060124120013/Muhamad Kemal Faza
Tanggal   : 29/09/2024

**************************************************************
DEFINISI DAN SPESIFIKASI TYPE
type garis : < p1 : point, p2 : point >
    <p1, p2> adalah sebuah garis yang terdiri dari dua titik yaitu titik awal (p1) dan titik akhir (p2)

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

StartP : garis ---> point
    StartP(G) mengembalikan titik awal dari garis G
EndP : garis ---> point
    EndP(G) mengembalikan titik akhir dari garis G

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakeGaris : 2 point ---> garis
    MakeGaris(p1,p2) membuat garis dengan titik awal p1 dan titik akhir p2

**************************************************************
DEFINISI DAN SPESIFIKASI OPERATOR

PanjangGaris : garis ---> integer
    PanjangGaris(G) menghitung panjang garis G
gradien : 2 garis ---> integer
    gradien(g1,g2) menghitung gradien garis g1 dan g2

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI PREDIKAT

IsSejajar : 2 garis ---> boolean
    IsSejajar(g1,g2) menentukan apakah garis g1 dan g2 sejajar

**************************************************************

REALISASI
**************************************************************
"""

from math import sqrt


def jarak(P1, P2):
    return sqrt(fx2(absis(P1) - absis(P2)) + fx2(ordinat(P1) - ordinat(P2)))


def fx2(x):
    return x * x


def MakePoint(x, y):
    return [x, y]


def absis(P):
    return P[0]


def ordinat(P):
    return P[1]


# Fungsi Utama


# Konstruktor
def MakeGaris(p1, p2):
    return [p1, p2]


# Selektor
def StartP(g):
    return g[0]


def EndP(g):
    return g[1]


# Operator
def PanjangGaris(g):
    return jarak(StartP(g), EndP(g))


def gradien(g):
    return (ordinat(EndP(g)) - ordinat(StartP(g))) / (absis(EndP(g)) - absis(StartP(g)))


# Predikat
def IsSejajar(g1, g2):
    return gradien(g1) == gradien(g2)


"""
APLIKASI
**************************************************************
"""

print(PanjangGaris(MakeGaris(MakePoint(0, 0), MakePoint(3, 4))))
print(
    IsSejajar(
        MakeGaris(MakePoint(0, 0), MakePoint(3, 4)),
        MakeGaris(MakePoint(-3, -4), MakePoint(0, 0)),
    )
)
