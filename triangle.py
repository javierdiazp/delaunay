import utils
from point import Point

class Triangle:
    def __init__(self, points, triangles):
        # pointers to each point, sorted by counter clockwise order
        if (utils.orient2D(points[0], points[1], points[2], 0.01) < 1):
            points = [points[1], points[0], points[2]]
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]

        # pointer to each adjacent triangle, sorted
        aux = [None]*3
        for i in range(0, 3):
          for t in triangles:
              if (t != None):
                  if (points[i] != t.p1 and
                      points[i] != t.p2 and
                      points[i] != t.p3):
                      aux[i] = t
                      break
        self.t1 = aux[0]
        self.t2 = aux[1]
        self.t3 = aux[2]

    def show(self):
        return "(" + self.p1.show() + ", " + self.p2.show() + ", " + self.p3.show() + ")" 

    'Input: point to check if its inside or out of this triangle, epsilon for orientation test'
    'Output: This triangle if it contains the point or lies in one of its edges, closest adjacent triangle if it lies outside of it.'
    def triangle_containing_point(self, point, eps):
        #Orientation tests
        firstEdgeTest = utils.orient2D(self.p1, self.p2, point, eps)
        secondEdgeTest = utils.orient2D(self.p2, self.p3, point, eps)
        thirdEdgeTest = utils.orient2D(self.p3, self.p1, point, eps)
        if firstEdgeTest >= 0 and secondEdgeTest >= 0 and thirdEdgeTest >= 0:
            return self
        elif firstEdgeTest < 0:
            return self.t3
        elif secondEdgeTest < 0:
            return self.t1
        else:
            return self.t2

