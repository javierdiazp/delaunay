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
        eps = 10
        minX = min(points, key=attrgetter('x')).x - eps
        minY = min(points, key=attrgetter('y')).y - eps
        maxX = max(points, key=attrgetter('x')).x + eps
        maxY = max(points, key=attrgetter('y')).y + eps

        # calculate the points of the triangle
        p0 = Point(minX,
                   minY)
        p1 = Point(maxX + maxY - minY,
                   minY)
        p2 = Point(minX,
                   maxY + maxX - minX)

        # set the triangle
        vertexs = [p0, p1, p2]
        neighbors = [None]*3
        
        return Triangle(vertexs, neighbors)

    ' POINT -> TRIANGLE '
    ' Find the triangle that contain a point in a triangulation'
    def findTriangle(self, point, eps):
        curTriangle = random.choice(self.triangles)
        while (curTriangle != curTriangle.approachToPoint(point, eps)):
            curTriangle = curTriangle.approachToPoint(point, eps)
            if (curTriangle == None):
                raise NameError("point lies outside any triangle")
        return curTriangle


    ' POINT -> VOID'
    ' Adds a point to the triangulation'
    def insertPoint(self, point):
        eps = 0.01
        if (self.triangles):
            # find the triangle containing the point
            t0 = self.findTriangle(point, eps)

            # does the point lies in the interior of the triangle?
            orientation = t0.edgesOrientation(point, eps)
            interior = orientation[0]*orientation[1]*orientation[2] != 0
            
            if (interior):
                # split into three triangles
                t1 = Triangle([t0.p1, t0.p2, point], [None]*3)
                t2 = Triangle([t0.p2, t0.p0, point], [None]*3)
                self.triangles.append(t1)
                self.triangles.append(t2)
                t0.p2 = point

                # update references to adjacent triangles
                t1.next0 = t2; t1.next1 = t0; t1.next2 = t0.next0
                t2.next0 = t0; t2.next1 = t1; t2.next2 = t0.next1
                t0.next0 = t1; t0.next1 = t2

                # legalize edges
                ' TODO '
                
            else:
                # get the other triangle
                neighbors0 = [t0.next0, t0.next1, t0.next2] # neighbors of t0
                for i in range(0, 3):
                    if (orientation[i] == 0):
                        t1 = neighbors[i]
                        n = i # index of t1 according to t0
                        break
                        
                # split into four triangles
                neighbors1 = [t1.next0, t1.next1, t1.next2] # neighbors of t1
                ve0 = [t0.p0, t0.p1, t0.p2] # vertexs of t0
                ve1 = [t0.p0, t0.p1, t0.p2] # vertexs of t1
                for i in range(0, 3):
                    if (ve1[i] != t0.p0 and t0.p1 != ve1[i] != t0.p2):
                        m = i # index of t0 according to t1
                        
                t2 = Triangle([ve0[(n+2)%3], ve0[n], point], [None]*3)
                t3 = Triangle([ve1[m], ve1[(m+1)%3], point], [None]*3)
                ve0[(n+2)%3] = point
                ve1[(m+1)%3] = point
                
                t0 = Triangle(ve0, neighbors0)
                t1 = Triangle(ve1, neighbors1)
                
                # update references to adjacent triangles
                ' TODO '

                # legalize edges
                ' TODO '
                    
        else:
            raise NameError("need at least one triangle")
