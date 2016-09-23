from point import Point

' POINT, POINT, POINT, DOUBLE -> BOOL '
' Return 0 if c lies on ab edge, 1 to the left and -1 to the right'
def orient2D(a, b, c, eps):
    det = (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)
    if (abs(det) <= abs(eps)):
        return 0
    else:
        return int(det/abs(det))
