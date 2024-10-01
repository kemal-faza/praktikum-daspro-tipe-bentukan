"""
Program   : Tanggal Setelahnya
Deskripsi : Menentukan tanggal berikutnya dari tanggal yang diinput
NIM/Nama  : 24060123140152/Kayis Hilmi Farih
Tanggal   : 10/31/2023
**************************************************************
DEFINISI DAN SPESIFIKASI TYPE
type Hr   : integer [1..31]
    definisi ini hanyalah untuk "menamakan" type integer dengan nilai tertentu supaya mewakili hari
type Bln  : integer [1..12]
    definisi ini hanyalah untuk "menamakan" type integer dengan nilai tertentu supaya mewakili bulan
type Thn  : integer > 0
    definisi ini hanyalah untuk "menamakan" type integer dengan nilai tertentu supaya mewakili tahun
type Date : < d : Hr, m : Bln, y : Thn >
    definisi ini hanyalah untuk "menamakan" tanggal pada hari d bulan m dan tahun y

**************************************************************
DEFINISI DAN SPESIFIKASI SELEKTOR

Day       : Date ---> integer
    Date(x) mengembalikan hari pada suatu tanggal
Month     : Date ---> integer
    Date(x) mengembalikan bulan pada suatu tanggal
Year      : Date ---> integer
    Date(x) mengembalikan tahun pada suatu tanggal

**************************************************************
DEFINISI DAN SPESIFIKASI KONSTRUKTOR

MakeDate  : <Hr,Bln,Thn> ---> date
    MakeDate(<Hr,Bln,Thn>) mendefinisikan tanggal pada hari Hr bulan Bln dan tahun Thn

**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI ANTARA

dpm       : Bln ---> integer
    dpm(m) memberikan jumlah hari pada tiap bulan dengan memperhitungkan tahun kabisat
dayToDate : Thn, integer ---> date
    dayToDate(y, totalDay) membuat tipe data tanggal dari tahun y setelah totalDay hari
    
**************************************************************
DEFINISI DAN SPESIFIKASI FUNGSI OPERATOR

NextDay   : date ---> date
    NextDay(date) menentukan tanggal keesokan harinya dari tanggal yang dimasukkan
Yesterday : date ---> date
    Yesterday(date) menentukan tanggal sehari sebelumnya dari tanggal yang dimasukkan
NextNDay  : date, integer ---> date
    NextNDay(date, n) menentukan tanggal berikutnya setelah n hari berlalu
HariKe1900 : date ---> integer
    HariKe1900(date) menghitung jumlah hari dari 1 Januari tahun bersangkutan hingga tanggal tersebut
**************************************************************
DEFINISI DAN SPESIFIKASI PREDIKAT

isKabisat : date ---> boolean
    isKabisat(y) menentukan apakah suatu tahun y adalah kabisat atau tidak
isEqD     : 2 date ---> boolean
    isEqD(date1, date2) menentukan apakah date1 dan date2 merupakan tanggal yang sama atau tidak
isBefore  : 2 date ---> boolean
    isBefore(date1, date2) menentukan apakah date1 adalah tanggal sebelum date2 atau tidak
isAfter   : 2 date ---> boolean
    isAfter(date1, date2) menentukan apakah date1 adalah tanggal setelah date2 atau tidak
    
**************************************************************

REALISASI
**************************************************************
"""


def MakeDate(d, m, y):
    return [d, m, y] if 1 <= d <= 31 and 1 <= m <= 12 else None


def Day(date):
    return date[0]


def Month(date):
    return date[1]


def Year(date):
    return date[2]


def isKabisat(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0


def isEqD(date1, date2):
    return (
        Day(date1) == Day(date2)
        and Month(date1) == Month(date2)
        and Year(date1) == Year(date2)
    )


def isBefore(date1, date2):
    return (
        Year(date1) < Year(date2)
        or Month(date1) < Month(date2)
        or Day(date1) < Day(date2)
    )


def isAfter(date1, date2):
    return (
        Year(date1) > Year(date2)
        or Month(date1) > Month(date2)
        or Day(date1) > Day(date2)
    )


def NextDay(date):
    if (
        Month(date) == 1
        or Month(date) == 3
        or Month(date) == 5
        or Month(date) == 7
        or Month(date) == 8
        or Month(date) == 10
    ):
        if Day(date) == 31:
            return MakeDate(1, Month(date) + 1, Year(date))
        else:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
    elif Month(date) == 2:
        if Day(date) == 28:
            if isKabisat(Year(date)):
                return MakeDate(Day(date) + 1, Month(date), Year(date))
            else:
                return MakeDate(1, Month(date) + 1, Year(date))
        else:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
    elif Month(date) == 12:
        if Day(date) == 31:
            return MakeDate(1, 1, Year(date) + 1)
        else:
            return MakeDate(Day(date) + 1, Month(date), Year(date))
    else:
        if Day(date) == 30:
            return MakeDate(1, Month(date) + 1, Year(date))
        else:
            return MakeDate(Day(date) + 1, Month(date), Year(date))


def Yesterday(date):
    if Day(date) == 1:
        if Month(date) == 1:
            return MakeDate(Day(date) + 30, Month(date) + 11, Year(date) - 1)
        elif Month(date) == 3:
            if isKabisat(Year(date)):
                return MakeDate(Day(date) + 28, Month(date) - 1, Year(date))
            else:
                return MakeDate(Day(date) + 27, Month(date) - 1, Year(date))
        elif (
            Month(date) == 2
            or Month(date) == 4
            or Month(date) == 6
            or Month(date) == 8
            or Month(date) == 9
            or Month(date) == 11
        ):
            return MakeDate(Day(date) + 30, Month(date) - 1, Year(date))
        else:
            return MakeDate(Day(date) + 29, Month(date) - 1, Year(date))
    else:
        return MakeDate(Day(date) - 1, Month(date), Year(date))


def dpm(m):
    if m == 1:
        return 1
    elif m == 2:
        return 32
    elif m == 3:
        return 60
    elif m == 4:
        return 91
    elif m == 5:
        return 121
    elif m == 6:
        return 152
    elif m == 7:
        return 182
    elif m == 8:
        return 213
    elif m == 9:
        return 244
    elif m == 10:
        return 274
    elif m == 11:
        return 305
    elif m == 12:
        return 335


def HariKe1900(date):
    return (
        dpm(Month(date))
        + Day(date)
        - 1
        + (1 if Month(date) > 2 and isKabisat(Year(date)) else 0)
    )


def dayToDate(y, totalDay):
    if totalDay <= 31:
        return MakeDate(totalDay, 1, y)
    elif totalDay <= (31 + (29 if isKabisat(y) else 28)):
        return MakeDate(totalDay - 31, 2, y)
    elif totalDay <= (62 + (29 if isKabisat(y) else 28)):
        return MakeDate(totalDay - (31 + (29 if isKabisat(y) else 28)), 3, y)
    elif totalDay <= (92 + (29 if isKabisat(y) else 28)):
        return MakeDate(totalDay - (62 + (29 if isKabisat(y) else 28)), 4, y)
    elif totalDay <= (123 + (29 if isKabisat(y) else 28)):
        return MakeDate(totalDay - (92 + (29 if isKabisat(y) else 28)), 5, y)
    elif totalDay <= (153 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (123 + (29 if isKabisat(y) else 28)),
            6,
            y,
        )
    elif totalDay <= (184 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (153 + (29 if isKabisat(y) else 28)),
            7,
            y,
        )
    elif totalDay <= (215 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (184 + (29 if isKabisat(y) else 28)),
            8,
            y,
        )
    elif totalDay <= (245 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (215 + (29 if isKabisat(y) else 28)),
            9,
            y,
        )
    elif totalDay <= (276 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (245 + (29 if isKabisat(y) else 28)),
            10,
            y,
        )
    elif totalDay <= (306 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (276 + (29 if isKabisat(y) else 28)),
            11,
            y,
        )
    elif totalDay <= (337 + (29 if isKabisat(y) else 28)):
        return MakeDate(
            totalDay - (306 + (29 if isKabisat(y) else 28)),
            12,
            y,
        )


def NextNDay(date, n):
    if HariKe1900(date) + n > (366 if isKabisat(Year(date)) else 365):
        return dayToDate(
            Year(date) + (n // 366 if isKabisat(Year(date)) else n // 365),
            (HariKe1900(date) + n)
            - (
                (366 if isKabisat(Year(date)) else 365)
                * (n // 366 if isKabisat(Year(date)) else n // 365)
            )
            - (
                (n // 366 if isKabisat(Year(date)) else n // 365)
                if isKabisat(
                    Year(date) + (n // 366 if isKabisat(Year(date)) else n // 365)
                )
                else 0
            ),
        )
    return dayToDate(
        Year(date),
        HariKe1900(date) + n,
    )


"""
APLIKASI
**************************************************************
"""
print(NextDay(MakeDate(1, 1, 2000)))
print(Yesterday(MakeDate(1, 1, 2000)))
print(NextNDay(MakeDate(1, 1, 2000), 100))
print(HariKe1900(MakeDate(10, 4, 2000)))
