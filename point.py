class Point:
    def __init__(self, x, y):
        self.x = x # coord x
        self.y = y # coord y

    def show(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
