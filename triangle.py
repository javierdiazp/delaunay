import utils
from point import Point

class Triangle:
    def __init__(self, points, triangles):
        # pointer to each point, sorted by counter clockwise order
        if (utils.orient2D(points[0], points[1], points[2], 0.01) < 1):
            points = [points[1], points[0], points[2]]
        self.p0 = points[0]
        self.p1 = points[1]
        self.p2 = points[2]

        # pointer to each adjacent triangle, sorted according to their opposite points
        aux = [None]*3
        for i in range(0, 3):
          for t in triangles:
              if (t != None and
                  points[i] != t.p0 and t.p1 != points[i] != t.p2):
                  aux[i] = t
                  break
        self.next0 = aux[0]
        self.next1 = aux[1]
        self.next2 = aux[2]

    ' POINT, DOUBLE -> LIST[INT] '
    ' Apply the orientation test to the edges of the triangle '
    def edgesOrientation(self, point, eps):
        #Orientation tests
        test0 = utils.orient2D(self.p1, self.p2, point, eps)
        test1 = utils.orient2D(self.p2, self.p0, point, eps)
        test2 = utils.orient2D(self.p0, self.p1, point, eps)
        return [test0, test1, test2]

    'Input: point to check if its inside or out of this triangle, epsilon for orientation test'
    'Output: This triangle if it contains the point or lies in one of its edges, closest adjacent triangle if it lies outside of it.'
    def approachToPoint(self, point, eps):
        orientation = self.edgesOrientation(point, eps)
        if (orientation[0] >= 0 and orientation[1] >= 0 and orientation[2] >= 0):
            return self
        elif orientation[0] < 0:
            return self.next0
        elif orientation[1] < 0:
            return self.next1
        else:
            return self.next2
        
    def show(self):
        return "(" + self.p0.show() + ", " + self.p1.show() + ", " + self.p2.show() + ")" 

