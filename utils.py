from point import Point

' POINT, POINT, POINT, DOUBLE -> INT '
' Return 0 if c lies on ab edge, 1 to the left and -1 to the right'
def orient2D(a, b, c, eps):
    det = (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)
    if (abs(det) <= eps):
        return 0
    else:
        return int(det/abs(det))

def incircle(a, b, c, d, eps):
    matrix = [[a.x, a.y, (a.x**2+a.y**2), 1],
              [b.x, b.y, (b.x**2+b.y**2), 1],
              [c.x, c.y, (c.x**2+c.y**2), 1],
              [d.x, d.y, (d.x**2+d.y**2), 1]]
    d = det(matrix, 1)

    if (abs(d) <= eps):
        return 0
    else:
        return int(d/abs(d))

def det(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * det(m, sign * matrix[0][i])
        return total

