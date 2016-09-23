class Point:
    def __init__(self, x, y):
        self.x = x # coord x
        self.y = y # coord y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def show(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
