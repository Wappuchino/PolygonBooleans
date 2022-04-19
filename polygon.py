import segment as s

"""
Defines a 2D closed polygon.

A polygon is defined here as a vertex loop with an edge
implied between consecutive vertices and between the first
and last vertices.
"""
class Polygon:
    def __init__(self, v):
        assert(len(v) >= 3)
        self.v = v

    def fold3(self, a_0, f):
        n = len(self.v)
        a = a_0
        for i in range(0, n):
            a = f(a, self.v[i], self.v[(i+1)%n], self.v[(i+2)%n])
        return a

    def is_degenerate(self):
        return self.fold3(
            False,
            lambda r, a, b, c: r or (s.turn2(a, b, c) == 0)
        )

    def is_convex(self):
        def compare_turn(r, a, b, c):
            t = s.turn2(a, b, c)
            return (
                r[0] if t == 0 else t,
                r[1] and (t * r[0] != -1)
            )
        
        return self.fold3((0, True), compare_turn)[1]

    def is_self_intersecting(self):
        return False
