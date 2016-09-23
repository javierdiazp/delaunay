import random
from operator import attrgetter

from point import Point
from triangle import Triangle
from triangulation import Triangulation

class DelaunayT(Triangulation):

    ' LIST[POINT] -> VOID '
    ' Initialize the Delaunay triangulation '
    def __init__(self, points):
        # set the initial triangle
        self.triangles = [self.auxTriangle(points)]

        # compute a random permutation of points
        random.shuffle(points)

        # insert points into the triangulation
        for p in points:
            self.insertPoint(p)

    ' LIST[POINT] -> TRIANGLE '
    ' Return a triangle that contain a set of points '
    def auxTriangle(self, points):
        # get the boundary of the set
        eps = 20
        minX = min(points, key=attrgetter('x')).x
        minY = min(points, key=attrgetter('y')).y
        maxX = max(points, key=attrgetter('x')).x
        maxY = max(points, key=attrgetter('y')).y

        # calculate the points of the triangle
        p1 = Point(minX - eps,
                   minY - eps)
        p2 = Point(maxX + maxY - minY + eps,
                   minY - eps)
        p3 = Point(minX - eps,
                   maxY + maxX - minX + eps)

        # set the triangle
        vertexs = [p1, p2, p3]
        neighbors = [None] * 3
        
        return Triangle(vertexs, neighbors)

    ' POINT -> TRIANGLE '
    ' Find the triangle that contain a point in a triangulation'
    def findTriangle(self, point, eps):
        curTriangle = random.choice(self.triangles)
        while(curTriangle != curTriangle.triangle_containing_point(point,eps) and curTriangle != None):
            curTriangle = curTriangle.triangle_containing_point(point,eps)
        if(curTriangle == None):
            raise NameError("Point lies outside any triangle")
        return curTriangle


    ' POINT -> VOID'
    ' Adds a point to the triangulation'
    def insertPoint(self, point):
        eps = 0.00001
        if self.triangles:
            t = findTriangle(point,eps)
            'TODO'
            if (True):
                pass
            else:
                pass
        else:
            raise NameError("need at least one triangle")
