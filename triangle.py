from point import Point
from edge import Edge

class Triangle:
    def __init__(self, points, triangles):
        'TODO: Ensure that the points are passed in CCW order, to do this'
        'sort the points based on x coordinate, if equal then by y coordinate'


        # pointer to each point
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]

        #Generate edges for each triangle
        self.e1 = Edge(self.p1,self.p2)
        self.e2 = Edge(self.p2,self.p3)
        self.e3 = Edge(self.p3,self.p1)

        'TODO: Ensure that pointers to adjacent triangles are in correct order'
        'that is, they match their corresponding edge inside the triangle.'

        # pointer to each adjacent triangle
        self.t1 = triangles[0]
        self.t2 = triangles[1]
        self.t3 = triangles[2]

    def show(self):
        return "(" + self.p1.show() + ", " + self.p2.show() + ", " + self.p3.show() + ")" 

    'Input: point to check if its inside or out of this triangle, epsilon for orientation test'
    'Output: This triangle if it contains the point or lies in one of its edges, closest adjacent triangle if it lies outside of it.'
    def triangle_containing_point(self,point,eps):
        #Orientation tests
        firstEdgeTest = self.e1.orientation_test(point,eps)
        secondEdgeTest = self.e2.orientation_test(point,eps)
        thirdEdgeTest = self.e3.orientation_test(point,eps)
        if firstEdgeTest >= 0 and secondEdgeTest >= 0 and thirdEdgeTest >= 0:
            return self
        elif firstEdgeTest < 0:
            return self.t1
        elif secondEdgeTest < 0:
            return self.t2
        else:
            return self.t3

