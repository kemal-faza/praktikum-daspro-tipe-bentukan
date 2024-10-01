def MakeP(x, y):
    return [x, y]


def Pemb(p):
    return p[0]


def Peny(p):
    return p[1]


def AddP(p1, p2):
    return MakeP(Pemb(p1) * Peny(p2) + Pemb(p2) * Peny(p1), Peny(p1) * Peny(p2))


def SubP(p1, p2):
    return MakeP(Pemb(p1) * Peny(p2) - Peny(p1) * Pemb(p2), Peny(p1) * Peny(p2))


def MulP(p1, p2):
    return MakeP(Pemb(p1) * Pemb(p2), Peny(p1) * Peny(p2))


def DivP(p1, p2):
    return MakeP(Pemb(p1) * Peny(p2), Peny(p1) * Pemb(p2))


def RealP(p):
    return p[0] / p[1]


def IsEqP(p1, p2):
    return Pemb(p1) * Peny(p2) == Peny(p1) * Pemb(p2)


def IsLtP(p1, p2):
    return Pemb(p1) * Peny(p2) < Peny(p1) * Pemb(p2)


def IsGtP(p1, p2):
    return Pemb(p1) * Peny(p2) > Peny(p1) * Pemb(p2)
