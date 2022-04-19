def sub2(lhs, rhs):
    return [lhs[0] - rhs[0], lhs[1] - rhs[1]]

def add2(lhs, rhs):
    return [lhs[0] + rhs[0], lhs[1] + rhs[1]]

def cross2(a, b, c):
    ab = sub2(b, a)
    ac = sub2(c, a)
    return ab[0] * ac[1] - ab[1] * ac[0]

def turn2(a, b, c):
    cp = cross2(a, b, c)
    return 1 if cp > 0 else (-1 if cp < 0 else 0)

def intersect2(a, b, c, d):
    return a
