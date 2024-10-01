"""
Program   : Range Nilai Mahasiswa
Deskripsi : Menentukan nilai tertinggi, terendah, dan range dari nilai suatu mata kuliah dari seorang mahasiswa
NIM/Nama  : 24060123140152/Kayis Hilmi Farih
Tanggal   : 10/31/2023
**************************************************************
DEFINISI DAN SPESIFIKASI TYPE

type mhs1 : <nim : string, nama : string, tanggalLahir : date>
    <nim, nama, tanggalLahir> adalah tipe data yang berisi data pribadi seorang mahasiswa
type mhs2 : <nim : string, kodeMatkul : string, nilai : integer>
    <nim, kodeMatkul, nilai> adalah tipe data yang berisi nilai suatu matkul seorang mahasiswa
type mhs3 : <kodeMatkul : string, namaMatkul : string>
    <kodeMatkul, namaMatkul> adalah tipe data yang berisi informasi mengenai suatu mata kuliah
type rangeNilai : <kodeMatkul : string, nilaiTertinggi : integer [0..100], nilaiTerendah : integer [0..100], selisih : integer [0..100]>
    <kodeMatkul, nilaiTertinggi, nilaiTerendah, selisih> adalah tipe data yang berisi range nilai mahasiswa pada suatu mata kuliah

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

kodeMatkul : mahasiswa ---> string
    kodeMatkul(mhs) mengembalikan kode mata kuliah dari mahasiswa mhs

nilai : mahasiswa ---> integer
    nilai(mhs) mengembalikan nilai dari mahasiswa mhs

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakeMhs1  : 2 string, date ---> mhs1
    MakeMhs2(nim, nama, tanggalLahir) membuat tipe data mhs1 yang terdiri dari <nim, nama, tanggalLahir>
MakeMhs2  : 2 string, integer ---> mhs2
    MakeMhs2(nim, kodeMatkul, nilai) membuat tipe data mhs2 yang terdiri dari <nim, kodeMatkul, nilai>
MakeMhs3  : 2 string, integer ---> mhs2
    MakeMhs2(kodeMatkul, namaMatkul) membuat tipe data mhs3 yang terdiri dari <kodeMatkul, namaMatkul>
MakeRangeNilai : string, 3 integer [0..100] ---> rangeNilai
    hitungRangeNilai(kodeMatkul, nilaiTertinggi, nilaiTerendah, selisih) membuat tipe data rangeNilai yang terdiri dari <kodeMatkul, nilaiTertinggi, nilaiTerendah, selisih>

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

min2   : 2 integer ---> integer
    min2(a, b) menentukan nilai terkecil antara a dan b
min4  : 4 integer ---> integer
    min4(a, b, c, d) menentukan nilai terkecil antara a, b, c, dan d
max2  : 2 integer ---> integer
    max2(a, b) menentukan nilai terbesar antara a dan b
max4  : 4 integer ---> integer
    max4(a, b, c, d) menentukan nilai terbesar antara a, b, c, dan d

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI OPERATOR

hitungRangeNilai : 4 mhs2 ---> rangeNilai
    hitungRangeNilai(m1, m2, m3, m4) menghitung range nilai dari m1, m2, m3, dan m4

**************************************************************

REALISASI
**************************************************************
"""


def MakeMhs1(nim, nama, tanggalLahir):
    return [nim, nama, tanggalLahir]


def MakeMhs3(kodeMatkul, namaMatkul):
    return [kodeMatkul, namaMatkul]


def MakeMhs2(nim, kodeMatkul, nilai):
    return [nim, kodeMatkul, nilai]


def MakeRangeNilai(kodeMatkul, nilaiTertinggi, nilaiTerendah, selisih):
    return [kodeMatkul, nilaiTertinggi, nilaiTerendah, selisih]


def kodeMatkul(mhs):
    return mhs[1]


def nilai(mhs):
    return mhs[2]


def min2(a, b):
    return a if a < b else b


def min4(a, b, c, d):
    return min2(min2(a, b), min2(c, d))


def max2(a, b):
    return a if a > b else b


def max4(a, b, c, d):
    return max2(max2(a, b), max2(c, d))


def hitungRangeNilai(m1, m2, m3, m4):

    return MakeRangeNilai(
        kodeMatkul(m1),
        max4(nilai(m1), nilai(m2), nilai(m3), nilai(m4)),
        min4(nilai(m1), nilai(m2), nilai(m3), nilai(m4)),
        max4(nilai(m1), nilai(m2), nilai(m3), nilai(m4))
        - min4(nilai(m1), nilai(m2), nilai(m3), nilai(m4)),
    )


print(
    hitungRangeNilai(
        MakeMhs2("24060124120013", "MIK1624102", 100),
        MakeMhs2("24060124120014", "MIK1624102", 80),
        MakeMhs2("24060124120015", "MIK1624102", 75),
        MakeMhs2("24060124120016", "MIK1624102", 85),
    )
)
