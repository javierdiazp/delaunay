from point import Point

#Utility class for edges
class Edge:
	def __init__(self,pointA,pointB):
		self.first = pointA
		self.second = pointB

	'Input: Point'
	'Output: Num'
	#Determinant of edge against point, used for orientation test.
	def det(self,point):
		return (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)


	'Input: Point, Num'
	'Output: 1 if the point is to the left of the edge, -1 if to the right, 0 if on the edge within epsilon value'
	#Orientation test, checks Edge against point.
	def orientation_test(self,point,eps):
		val = det(point)
		if(abs(val) < eps):
			return 0
		elif val > eps:
			return 1
		else:
			return -1

	def show(self):
		return '[ ' + self.first.show() + ', ' + self.second.show() + ']'

