from point import Point

class Triangle:
    def __init__(self, points, triangles):
        # pointer to each point
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]

        # pointer to each adjacent triangle
        self.t1 = triangles[0]
        self.t2 = triangles[1]
        self.t3 = triangles[2]

    def show(self):
        return "(" + self.p1.show() + ", " + self.p2.show() + ", " + self.p3.show() + ")" 
