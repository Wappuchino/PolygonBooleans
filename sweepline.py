import segment

def sweepline(e, s_0, f):
    s = s_0
    for e_i in e:
        s = f(s, e_i)
    return s

def intersect(l):
    e = []
    for l_i in l:
        e.append((l_i[0][0], False, l_i))
        e.append((l_i[1][0], True, l_i))
    e.sort()
    def update_sweep(s, l_i):
        (intersections, state) = s
        if segment.intersect2():
        return (intersections, state)
    return sweepline(e, ([], []), update_sweep)[0]
